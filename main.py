from pyscript import document

# Class that stores each classmate's future profession info
class futureprof:

    # Initialize attributes for each classmate
    def __init__(self, name, section, profession):
        self.name = name
        self.section = section
        self.profession = profession

    # Returns a formatted introduction string
    def introduce(self):
        return f"👋 Hello, my name is {self.name} from Grade 10 {self.section}. My future profession is {self.profession}. 🫡"


# List that stores all classmate objects
classmates = [
    futureprof("KC", "Sapphire", "Doctor"),
    futureprof("Luis", "Sapphire", "Engineer"),
    futureprof("Sophia", "Sapphire", "Architect"),
    futureprof("Javier", "Sapphire", "Pilot"),
    futureprof("Briana", "Sapphire", "Teacher")
]


# Adds a new classmate from input fields
def addClassmate(event):
    user = document.getElementById("name").value
    section = document.getElementById("section").value
    profession = document.getElementById("Future_profession").value

    # Create new object and store it in list
    new_classmate = futureprof(user, section, profession)
    classmates.append(new_classmate)

    # Show success message
    document.getElementById("notif").innerHTML = "✅ Classmate added successfully!"


# Displays all classmates in formatted output
def showlist(event):
    output = ""

    # Loop through all classmates and display introductions
    for classmate in classmates:
        output += f"""
        <div style="
            padding: 10px;
            margin-bottom: 10px;
            border-left: 4px solid #ffd700;
            background: rgba(255,255,255,0.08);
            border-radius: 10px;
        ">
            {classmate.introduce()}
        </div>
        """

    document.getElementById("classmate-list").innerHTML = output