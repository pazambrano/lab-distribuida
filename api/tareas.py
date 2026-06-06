from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Tarea(BaseModel):
    id: Optional[int] = None
    titulo: str
    descripcion: str
    completada: bool = False

tareas: List[Tarea] = []

@app.get("/api/tareas")
async def listar_tareas():
    return tareas

@app.post("/api/tareas")
async def crear_tarea(tarea: Tarea):
    tarea.id = len(tareas) + 1
    tareas.append(tarea)
    return {"mensaje": "Tarea creada exitosamente", "tarea": tarea}

@app.delete("/api/tareas/{tarea_id}")
async def eliminar_tarea(tarea_id: int):
    for i, tarea in enumerate(tareas):
        if tarea.id == tarea_id:
            del tareas[i]
            return {"mensaje": "Tarea eliminada exitosamente"}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")
