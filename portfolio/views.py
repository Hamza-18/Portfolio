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


class Skill:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def getLevel(self):
        return self.level

    def getName(self):
        return self.name


def create_skills_section():
    # Frontend
    front_end_skills = [Skill("HTML", 90, ), Skill("CSS", 90), Skill("Javascript", 90), Skill("React", 90)]
    front_end = SkillSection("Frontend Developer", "uil uil-brackets-curly skills_icon", front_end_skills, "skill_open")
    # backend skills
    backend_skills = [Skill("Django", 90, ), Skill("SQL", 90), Skill("Java", 90)]
    back_end = SkillSection("Backend Developer", "uil uil-server", backend_skills, "skill_close")
    return [front_end,back_end]

my_skills = create_skills_section()


def index(request):
    return render(request, "portfolio/index.html", {
        "skills": my_skills
    })
