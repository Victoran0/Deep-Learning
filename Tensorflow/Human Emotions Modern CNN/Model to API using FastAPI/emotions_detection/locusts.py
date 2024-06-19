from locust import SequentialTaskSet, HttpUser, task


class DetectorTask(SequentialTaskSet):
    @task
    def detection(self):
        with open("test_image.jpg", "rb") as image:
            self.client.post(
                "/detect",
                files={'im': image}
            )


class LoadTester(HttpUser):
    host = "url"
    tasks = [DetectorTask]
