from locust import HttpUser, TaskSet, task


class UserBehaviour(TaskSet):
    @task
    def login_post(self):
        url = "http://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=7f327e998f4054a872bfde217b393160"
        payload = {}
        headers = {}
        self.client.get(url,headers=headers,data=payload)


class User(HttpUser):
    task_set = UserBehaviour
    min_wait = 100
    max_wait = 500
    host = "http://api.openweathermap.org/data/2.5/weather?q=London&appid=7f327e998f4054a872bfde217b393160"
