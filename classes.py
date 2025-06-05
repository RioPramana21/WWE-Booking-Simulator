class Superstar:
    def __init__(self, name, overall_rating):
        self.name = name
        self.overall_rating = overall_rating
        self.alignment = "Face"
    
    def __str__(self):
        return f"{self.name} (Overall Rating: {self.overall_rating})"