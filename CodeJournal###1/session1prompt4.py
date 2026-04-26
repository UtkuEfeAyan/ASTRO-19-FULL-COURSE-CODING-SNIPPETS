#parent class animal
class Animal:
    def __init__(self, has_arms, length_of_arms, has_legs, length_of_legs,
                    has_eyes, number_of_eyes, have_tail, tail_length, 
                        is_furry, furr_pattern):

        self.has_arms = has_arms
        if has_arms:
            self.length_of_arms = length_of_arms
        else:
            self.length_of_arms = 0
        
        self.has_legs = has_legs
        if has_legs:
            self.length_of_legs = length_of_legs
        else:
            self.length_of_legs = 0
            
        self.has_eyes = has_eyes
        if has_eyes:
            self.number_of_eyes = number_of_eyes
        else:
            self.number_of_eyes = 0
    
        self.have_tail = have_tail
        if have_tail:
            self.tail_length = tail_length
        else:
            self.tail_length = 0

        self.is_furry = is_furry
        if is_furry:
            self.furr_pattern = furr_pattern
        else:
            self.furr_pattern = "No fur"

    def describe(self):
        print(f"Has arms: {self.has_arms}")
        print(f"Length of arms: {self.length_of_arms} meters")
        print(f"Has legs: {self.has_legs}")
        print(f"Length of legs: {self.length_of_legs} meters")
        print(f"Has eyes: {self.has_eyes}")
        print(f"Number of eyes: {self.number_of_eyes}")
        print(f"Has tail: {self.have_tail}")
        print(f"Tail length: {self.tail_length} meters")
        print(f"Is furry: {self.is_furry}")
        print(f"Fur pattern: {self.furr_pattern}")

#subclass cat that inherits from animal enabling multiple animal clases for future
#with copy paste ready kind of structure still needs to be called at main to show up in output
class Cat(Animal):
    def __init__(self, has_arms, length_of_arms, has_legs, length_of_legs,
                    has_eyes, number_of_eyes, have_tail, tail_length, 
                        is_furry, furr_pattern, breed):
        #super method that pulls from the parent class
        super().__init__(has_arms, length_of_arms, has_legs, length_of_legs,
                         has_eyes, number_of_eyes, have_tail, tail_length,
                         is_furry, furr_pattern)
        self.breed = breed

    def describe(self):
        #super method that pulls from the parent class
        super().describe()
        print(f"Breed: {self.breed}")   

def main():
    #put value to attributes accurate to cats
    cat = Cat(False, 0, True, 0.25, True, 2, True, 0.32, True, "Tuxedo", "Bobcat/Domestic Shorthair Mix")
    cat.describe()

if __name__ == "__main__":
    main()

#date: 2026-04-01