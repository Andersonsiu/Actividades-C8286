from locust import HttpUser, TaskSet, task, between

class RecomendacionesTaskSet(TaskSet):
    
    @task
    def obtener_recomendaciones(self):
        user_id = 'user_1'  # Asegúrate de usar un user_id válido
        response = self.client.post("/recomendaciones", json={"user_id": user_id})
        if response.status_code != 200:
            print(f"Error: {response.status_code}, {response.text}")

class WebsiteUser(HttpUser):
    tasks = [RecomendacionesTaskSet]
    wait_time = between(1, 5)

