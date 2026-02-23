from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
import requests
FIREBASE_URL = "https://mayaedu-accounts-default-rtdb.firebaseio.com/"
# Create your views here.
def loading(request):
  return render(request, "loading.html")
def index(request):
  return render(request, "index.html")
def course(request):
  return render(request, "course.html") 
def about(request):
  return render(request, "about.html") 
def contact(request):
  return render(request, "contact.html")
"""def signup(request):
    success = False
    if request.method == "POST":
        fullname = request.POST.get("fullname").replace(" ", "_")
        class_name = request.POST.get("class_name").lower()
        sex = request.POST.get("sex")
        code = request.POST.get("code")
        
        if code == "#maya/notes/01234567890":
            student_data = {
                fullname: {
                    "fullname": fullname,
                    "sex": sex,
                    "classcaptain": "none"
                }
            }
            url = f"{FIREBASE_URL}/students/{class_name}.json"
            response = requests.patch(url, json=student_data)
            
            if response.status_code == 200:
                success = True  # mark success
                redirect("/index/")
        else:
          return redirect("/error/")
    
    return render(request, "signup.html", {"success": success})"""
"""def signup(request):
  if request.method == "POST":
    fullname = request.POST.get("fullname").replace(" ", "_")
    class_name = request.POST.get("class_name").lower()
    sex = request.POST.get("sex")
    code = request.POST.get("code")
    student_data = {
        fullname: {
            "fullname": fullname,
            "sex": sex,
            "classcaptain": "none"
          }
      }
    url = f"{FIREBASE_URL}/students/{class_name}.json"
    response = requests.patch(url, json=student_data)
    print(response.status_code)
    print(response.text)          
    if response.status_code == 200:
      return redirect("/index/")
  return render(request, "signup.html")"""
def signup(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        class_name = request.POST.get("class_name")
        sex = request.POST.get("sex")
        code = request.POST.get("code")

        if not fullname or not class_name:
            return HttpResponse("Missing data")

        if code != "#maya/notes/01234567890":
            return HttpResponse("Invalid code")

        fullname = fullname.replace(" ", "_")
        class_name = class_name.lower()

        student_data = {
            fullname: {
                "fullname": fullname,
                "sex": sex,
                "classcaptain": "none"
            }
        }

        url = f"{FIREBASE_URL}/students/{class_name}.json"
        response = requests.patch(url, json=student_data)

        print(response.status_code)
        print(response.text)

        if response.status_code == 200:
            return redirect("/index/")
        else:
            return HttpResponse("Firebase error")

    return render(request, "signup.html")  