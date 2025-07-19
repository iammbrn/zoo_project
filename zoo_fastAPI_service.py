from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from typing import List, Dict
import threading
from create_type import CreateType
from location import Location
from breeding import Breeding
from hunting import Hunting

app = FastAPI(title="Zoo Visualizer")
templates = Jinja2Templates(directory="templates")

class ZooSimulation:
    def __init__(self):
        self.lock = threading.Lock()
        self.reset()
        self.last_new_animals = []
        self.last_removed_animals = []

    def reset(self):
        with self.lock:
            self.create_type = CreateType()
            self.all_types_dict = self.create_type.create_animals()
            self.location = Location()
            self.current_locations = self.location.random_current_location_generation(self.all_types_dict)
            self.step = 0
            self.max_steps = 1000
            self.last_new_animals = []
            self.last_removed_animals = []

    def step_forward(self):
        with self.lock:
            if self.step >= self.max_steps:
                return self.get_animals(), [], []
            # Önceki hayvan id'lerini kaydet
            prev_ids = set()
            for animal_type, animal_list in self.current_locations.items():
                for animal in animal_list:
                    prev_ids.add((animal_type, animal[0]))
            breeding = Breeding()
            new_breedings = breeding.calculate_distance_for_breeding(self.current_locations)
            hunting = Hunting()
            new_huntings = hunting.calculate_distance_for_hunting(new_breedings)
            new_directions = self.location.random_direction_generation(new_huntings)
            new_locations = self.location.calculate_new_location(new_directions)
            # Sonraki hayvan id'lerini kaydet
            next_ids = set()
            for animal_type, animal_list in new_locations.items():
                for animal in animal_list:
                    next_ids.add((animal_type, animal[0]))
            new_animals = list(next_ids - prev_ids)
            removed_animals = list(prev_ids - next_ids)
            self.current_locations = new_locations
            self.step += 1
            self.last_new_animals = new_animals
            self.last_removed_animals = removed_animals
            return self.get_animals(), new_animals, removed_animals

    def run_to_end(self):
        with self.lock:
            while self.step < self.max_steps:
                self.step_forward()
            return self.get_animals(), self.last_new_animals, self.last_removed_animals

    def get_animals(self):
        # İngilizce tür isimlerini frontend ile uyumlu Türkçe isimlere çevir
        type_map = {
            "female_sheep_list": ("koyun", "dişi"),
            "male_sheep_list": ("koyun", "erkek"),
            "female_cow_list": ("inek", "dişi"),
            "male_cow_list": ("inek", "erkek"),
            "female_chicken_list": ("tavuk", "dişi"),
            "male_cockerel_list": ("horoz", "erkek"),
            "female_wolf_list": ("kurt", "dişi"),
            "male_wolf_list": ("kurt", "erkek"),
            "female_lion_list": ("aslan", "dişi"),
            "male_lion_list": ("aslan", "erkek"),
            "hunter": ("avci", None)
        }
        animals = []
        for animal_type, animal_list in self.current_locations.items():
            type_tr, gender = type_map.get(animal_type, (animal_type, None))
            for animal in animal_list:
                # animal = [id, hareket_kapasitesi, (x, y)]
                id = animal[0]
                move_capacity = animal[1]
                x, y = animal[2]
                animals.append({
                    "name": f"{type_tr}_{id}",
                    "x": int(round(x)),
                    "y": int(round(y)),
                    "gender": gender,
                    "type": type_tr,
                    "raw_type": animal_type,
                    "id": id
                })
        return animals

zoo_simulation = ZooSimulation()

@app.get("/", response_class=HTMLResponse)
async def render_map(request: Request):
    return templates.TemplateResponse("zoo_map.html", {"request": request})

@app.get("/api/step")
async def api_step():
    animals, new_animals, removed_animals = zoo_simulation.step_forward()
    return JSONResponse(content={"animals": animals, "step": zoo_simulation.step, "new_animals": new_animals, "removed_animals": removed_animals})

@app.get("/api/reset")
async def api_reset():
    zoo_simulation.reset()
    animals, new_animals, removed_animals = zoo_simulation.step_forward()
    return JSONResponse(content={"animals": animals, "step": zoo_simulation.step, "new_animals": new_animals, "removed_animals": removed_animals})

@app.get("/api/final")
async def api_final():
    if zoo_simulation.step >= zoo_simulation.max_steps:
        return JSONResponse(content={"error": "Simülasyon zaten 1000. adımda.", "animals": zoo_simulation.get_animals(), "step": zoo_simulation.step, "new_animals": [], "removed_animals": []})
    animals, new_animals, removed_animals = zoo_simulation.run_to_end()
    return JSONResponse(content={"animals": animals, "step": zoo_simulation.step, "new_animals": new_animals, "removed_animals": removed_animals})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("zoo_fastAPI_service:app", host="0.0.0.0", port=8000, reload=True)