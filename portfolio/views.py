from django.shortcuts import render


# Create your views here.
class SkillSection:
    def __init__(self, header, icon, skills, skill_open=""):
        self.header = header
        self.icon = icon
        self.skills = skills
        self.open = skill_open

    def getHeader(self):
        return self.header

    def getIcon(self):
        return self.icon

    def getSkills(self):
        return self.skills

def create_skills_section():
    # Frontend
    front_end_skills = ["HTML","CSS", "Javascript","React"]
    front_end = SkillSection("Frontend Developer", "uil uil-brackets-curly skills_icon", front_end_skills, "skill_open")
    # backend skills
    backend_skills = ["Django","SQL", "Java","Firebase"]
    back_end = SkillSection("Backend Developer", "uil uil-server", backend_skills, "skill_close")
    # Desktop development
    desktop_skills = ["Java Swing", "SQL"]
    desktop = SkillSection("Desktop Development", "uil uil-desktop", desktop_skills, "skill_close")
    # Mobile Development
    mobile_skills = ["Android", "Flutter", "Java", "Firebase"]
    mobile = SkillSection("Application Development", "uil uil-mobile-android", mobile_skills, "skill_close")

    # game development
    game_skills = ["Unity", "C#"]
    game = SkillSection("Game Development", "uil uil-icons", game_skills, "skill_close")

    # programming languages
    language_skills = ["Python", "Java", "C#", "Javascript", "Dart", "Haskell", "Assembly Language"]
    programming = SkillSection("Programming Languages", "uil uil-java-script", language_skills, "skill_close")
    return [front_end, back_end, desktop, mobile, game, programming]


my_skills = create_skills_section()


def index(request):
    return render(request, "portfolio/index.html", {
        "skills": my_skills
    })
