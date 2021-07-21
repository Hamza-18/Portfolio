from django.http import HttpResponse, HttpResponseNotFound
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


class Service:
    def __init__(self, heading, sub_heading, icon, services):
        self.icon = icon
        self.heading = heading
        self.sub_heading = sub_heading
        self.services = services

    def get_icon(self):
        return self.icon

    def get_heading(self):
        return self.heading

    def get_sub_heading(self):
        return self.sub_heading

    def get_services(self):
        return self.services


class Project:
    def __init__(self, icon, heading, description, width, height,subtitle = ""):
        self.icon = icon
        self.heading = heading
        self.description = description
        self.width = width
        self.height = height
        self.sub_title = subtitle

    def get_sub_title(self):
        return self.sub_title

    def get_icon(self):
        return self.icon

    def get_heading(self):
        return self.heading

    def get_description(self):
        return self.description

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


def create_skills_section():
    # Frontend
    front_end_skills = ["HTML", "CSS", "Javascript", "React"]
    front_end = SkillSection("Frontend Developer", "uil uil-brackets-curly skills_icon", front_end_skills, "skill_open")
    # backend skills
    backend_skills = ["Django", "SQL", "Java", "Firebase"]
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


def create_services():
    android_services = ["APK file of the application",
                        "Responsive UI for different devices",
                        "Source code if in contract",
                        "Submission on Play Store if required", ]
    android_application = Service("Android", "Application", "uil uil-android service_icon",
                                  android_services)

    desktop_services = ["I will provide .exe or JAR file according to your requirements ",
                        "Responsive UI for different screen size",
                        "Database connectivity"]
    desktop_application = Service("Desktop", "Application", "uil uil-desktop service_icon", desktop_services)

    web_services = ["Responsive UI for different devices",
                    "Server side configuration",
                    "Database connectivity"]
    web_application = Service("Web", "Application", "uil uil-brackets-curly service_icon", web_services)

    game_service = ["3D/2D game built in Unity",
                    "Android apk file or IOS equivalent",
                    "Submission on play store if required"]
    game_development = Service("Game", "Development", "uil uil-icons", game_service)
    return [android_application, desktop_application, web_application, game_development]


def create_projects():
    cupshup = Project("/static/projects/cupshup/cupshup.png", "Food Delivery App", "Native Android App built using Java", 200,
                      200,"cupshup")
    java_swing = Project("/static/projects/booknbed/login.png", "Management System", "Java swing application built for windows",
                         400, 400,"booknbed")
    pong = Project("/static/projects/pong/pong.png","Pong","Pong built using Typescript and rxjs library",300,300,"pong")
    return [cupshup, java_swing, pong]

def create_project_dict():
    cupshup_img =["/static/projects/cupshup/cupshup.png",
                  "/static/projects/cupshup/menu.png",
                  "/static/projects/cupshup/sub_menu.png",
                  "/static/projects/cupshup/cart.png"]
    cupshup_desc = "Cupshup is a food delivery app built for a restaurant in Lahore, Pakistan. It is a native android app built using Java. " \
                   "The main functionality of this app is to show menu and take order from the user. Once the order is placed " \
                   "it is saved in the database which is implemented using google firebase. On admin side the database is" \
                   " fetched and all the orders are shown. I also implemented push notification for the admin using service." \
                   " The app also gets the current location of user using GPS and admin can also add promo codes through firebase" \
                   " which will be shown on the main activity of app."
    cupshup = Project(cupshup_img,"CupShup",cupshup_desc,200,200,"Food delivery app")

    booknbed_img = ["/static/projects/booknbed/login.png",
                    "/static/projects/booknbed/dashboard.png",
                    "/static/projects/booknbed/students.png",
                    "/static/projects/booknbed/add.png"]
    booknbed_desc = "This is a hostel management system built for a hostel in Lahore, Pakistan." \
                    " It is built for windows using Java Swing and  MySQL" \
                    " It has all the functionalities to add, update, delete for " \
                    " students and staff. It also notifies when fee is due of a student."
    booknbed = Project(booknbed_img,"Book & Bed",booknbed_desc,400,400,"Hostel Management System")
    projects = {"cupshup":cupshup,"booknbed":booknbed}
    return projects
my_skills = create_skills_section()
my_services = create_services()
my_projects = create_projects()


def index(request):
    return render(request, "portfolio/index.html", {
        "skills": my_skills,
        "services": my_services,
        "projects": my_projects
    })

def project(request,proj_name):
    try:
        my_project = create_project_dict()[proj_name]
        return render(request,"portfolio/project.html",{
            "project": my_project
        })
    except :
        return HttpResponseNotFound("Page not found")