from schemas.policy import PolicySchemaAdd
from utils.repository import AbstractRepository


class PolicyService:
    def __init__(self, tasks_repo: AbstractRepository):
        self.tasks_repo: AbstractRepository = tasks_repo()

    async def add(self, task: PolicySchemaAdd):
        tasks_dict = task.model_dump()
        task_id = await self.tasks_repo.add(tasks_dict)
        return task_id

    async def get(self):
        tasks = await self.tasks_repo.find_all()
        return tasks