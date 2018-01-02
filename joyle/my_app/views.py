from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .models import Task, Project
import json

def index(request):
    return HttpResponse('Hello world from Nginx->Tornado->Django')

def home_view(request):
    return render(request, 'my_app/home.html', {})

def tasks_page(request):
    tasks = Task.objects.all()
    content = { 'tasks' : tasks }
    return render(request, 'my_app/home.html', content)

@csrf_exempt
@login_required(login_url='/auth/error')
def projects_view(request, project_id):
    resp = {}
    if request.method == "GET":
        resp = project_get(request, project_id)
    elif request.method == "POST":
        resp = project_post(request)
    elif request.method == "PUT":
        resp = project_put(request, project_id)
    elif request.method == "DELETE":
        resp = project_delete(project_id)
    else:
        resp['result'] = 'failed'
        resp['errors'] = 'invalid HTTP request method'
    return HttpResponse(json.dumps(resp), content_type='application/json')


@csrf_exempt
@login_required(login_url='/auth/error')
def task_view(request, task_id):
    resp = {}
    if request.method == "GET":
        resp = task_get(request, task_id)
    elif request.method == "POST":
        resp = task_post(request, task_id)
    elif request.method == "PUT":
        resp = task_put(request, task_id)
    elif request.method == "DELETE":
        resp =task_delete(task_id)
    else:
        resp['result'] = 'failed'
        resp['errors'] = 'invalid HTTP request method'
    return HttpResponse(json.dumps(resp), content_type='application/json')

# Create your views here.

def task_get(request, task_id):
    resp_data = {}
    json_data = {}
    if task_id != "":
        try:
            task_id = int(task_id)
            task = Task.objects.get(pk=task_id)
            json_data = {
              'id': task_id,
              'name': task.name,
              'description': task.description,
              'create_date': str(task.create_date),
              'deadline': str(task.deadline),
              'position': task.position,
              'level': task.parent,
              'parent': task.parent,
              'has_child': task.has_child,
              'project': str(task.project)
            }
            resp_data['result'] = "OK"
            resp_data['errors'] = ""
            resp_data['data'] = json_data
        except ObjectDoesNotExist:
            resp_data['result'] = "failed"
            resp_data['errors'] = "task doesn't exist"

    elif len(request.GET) > 0:
        prog_id = request.GET['project']
        prog_id = int(prog_id)
        if prog_id > 0:
            try:
                proj = Project.objects.get(pk=prog_id)
                task = Task.objects.get(project=proj)
                json_data = {
                  'id': task_id,
                  'name': task.name,
                  'description': task.description,
                  'create_date': str(task.create_date),
                  'deadline': str(task.deadline),
                  'position': task.position,
                  'level': task.parent,
                  'parent': task.parent,
                  'has_child': task.has_child,
                  'project': str(task.project)
                }
                resp_data['result'] = "OK"
                resp_data['errors'] = ""
                resp_data['data'] = json_data
            except:
                resp_data['result'] = 'failed'
                resp_data['errors'] = 'Task with this project does not exist'
        else:
            resp_data['result'] = 'failed'
            resp_data['errors'] = 'prog_id should be GT 0'
    else:
        tasks = []
        resp_data['result'] = "OK"
        resp_data['errors'] = ""
        resp_data['data'] = tasks
        ids = iter(Task.objects.all().values_list('id', flat=True))
        for task in Task.objects.all():
            tasks.append({
                'id': next(ids),
                'name': task.name,
                'description': task.description,
                'create_date': str(task.create_date),
                'deadline': str(task.deadline),
                'position': task.position,
                'level': task.level,
                'parent': task.parent,
                'has_child': task.has_child,
                'project': str(task.project)
            })
    return resp_data

def task_post(request, task_id):
    resp_data = {}
    data = json.loads(request.body)
    #try:
    m_project = Project.objects.get(pk=data['data']['project'])
    task = Task.objects.create(
            name = data['data']['name'], 
            description = data['data']['description'],
            create_date = data['data']['create_date'],
            deadline = data['data']['deadline'],
            position = data['data']['position'],
            level = data['data']['level'],
            parent = data['data']['parent'],
            has_child = data['data']['has_child'],
            project = m_project                   
        )
    task.save()
    resp_data["result"] = "OK"
    resp_data["errors"] = ""
#    except:
#        resp_data["result"] = "failed"
#        resp_data["errors"] = "create DB object using ORM error"
    return resp_data

def task_put(request, task_id):
    resp_data = {}
    data = json.loads(request.body)
    if task_id != "":
        task_id = int(task_id)
        if task_id > 0:
            task = Task.objects.get(pk=task_id)
            try:
                task.name = data['data']['name']
                task.description = data['data']['description']
                task.create_date = data['data']['create_date']
                task.deadline = data['data']['deadline']
                task.position = data['data']['position']
                task.level = data['data']['level']
                task.parent = data['data']['parent']
                task.has_child = data['data']['has_child']
                task.project = data['data']['project']
                task.save()

                resp_data['result'] = "OK"
                resp_data['errors'] = ""
            except:
                resp_data['result'] = "failed"
                resp_data['errors'] = "update DB object using ORM error"
        else:
            resp_data['result'] = "failed"
            resp_data['errors'] = "task_id should be GT 0"
    else:
        resp_data['result'] = "failed"
        resp_data['errors'] = "no matches for task_id"
    return resp_data

def task_delete(task_id):
    resp_data = {}
    if task_id != "":
        task_id = int(task_id)
        if task_id > 0:
            try:
                Task.objects.get(pk=task_id).delete()
                resp_data['result'] = "OK"
                resp_data['errors'] = ""
            except Exception as e:
                resp_data['result'] = "failed"
                resp_data['errors'] = "object doesn't exist"
        else:
            resp_data['result'] = "failed"
            resp_data['errors'] = "task_id should be GT 0"
    else:
        resp_data['result'] = "failed"
        resp_data['errors'] = "no matches for task_id"
    return resp_data


def project_get(request, project_id):
    resp_data = {}
    if project_id != "":
        try:
            project_id = int(project_id)
            project = Project.objects.get(pk=project_id)
            json_data = {
              'id': project_id,
              'name': project.name,
              'create_date': str(project.create_date),
              'deadline': str(project.deadline),
            }
            resp_data['result'] = "OK"
            resp_data['errors'] = ""
            resp_data['data'] = json_data
        except ObjectDoesNotExist:
            resp_data['result'] = "failed"
            resp_data['errors'] = "project doesn't exist"
    else:
        projects = []
        resp_data['result'] = "OK"
        resp_data['errors'] = ""
        resp_data['data'] = projects
        ids = iter(Project.objects.all().values_list('id', flat=True))
        for project in Project.objects.all():
            projects.append({
                'id': next(ids),
                'name': project.name,
                'create_date': str(project.create_date),
                'deadline': str(project.deadline),
            })    
    return resp_data

def project_post(request):
    resp_data = {}
    try:
        data = json.loads(request.body)
        project = Project.objects.create(
          name = data['data']['name'],
          create_date = data['data']['create_date'],
          deadline = data['data']['deadline']
        )
        project.save()
        resp_data['result'] = 'Project created'
        resp_data['errors'] = ''
    except:
        resp_data['result'] = 'failed'
        resp_data['erros'] = 'Error creating project'
    return resp_data

def project_put(request, project_id):
    resp_data = {}
    data = json.loads(request.body)
    if project_id != "":
        project_id = int(project_id)
        if project_id > 0:
            project = Project.objects.get(pk=project_id)
            try:
                project.name = data['data']['name']
                project.create_date = data['data']['create_date']
                project.deadline = data['data']['deadline']
                project.save()

                resp_data['result'] = "OK"
                resp_data['errors'] = ""
            except:
                resp_data['result'] = "failed"
                resp_data['errors'] = "update DB object using ORM error"
        else:
            resp_data['result'] = "failed"
            resp_data['errors'] = "project_id should be GT 0"
    else:
        resp_data['result'] = "failed"
        resp_data['errors'] = "no matches for project_id"
    return resp_data

def project_delete(project_id):
    resp_data = {}
    if project_id != "":
        project_id = int(project_id)
        if project_id > 0:
            try:
                Project.objects.get(pk=project_id).delete()
                resp_data['result'] = "OK"
                resp_data['errors'] = ""
            except:
                resp_data['result'] = "failed"
                resp_data['errors'] = "object doesn't exist"
        else:
            resp_data['result'] = "failed"
            resp_data['errors'] = "project_id should be GT 0"
    else:
        resp_data['result'] = "failed"
        resp_data['errors'] = "no matches for project_id"
    return resp_data
