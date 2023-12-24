from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Materi
from .forms import CourseForm, MateriForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

def edit_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'add_course.html', {'form': form, 'course': course})

def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    return redirect('course_list')

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    materis = course.materi.all()
    return render(request, 'course_detail.html', {'course': course, 'materi': materis})

# matri
def materi_list(request):
    materi = Materi.objects.all()
    return render(request, 'materi.html', {'materi': materi})

def create_materi(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = MateriForm(request.POST)
        if form.is_valid():
            materi = form.save(commit=False)
            materi.course = course
            materi.save()
            return redirect('course_detail', course_id=course.id)
    else:
        form = MateriForm()
    return render(request, 'add_materi.html', {'form': form, 'course': course})

def edit_materi(request, materi_id):
    materi = get_object_or_404(Materi, pk=materi_id)
    if request.method == 'POST':
        form = MateriForm(request.POST, instance=materi)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = MateriForm(instance=materi)
    return render(request, 'add_materi.html', {'form': form, 'materi': materi})

def delete_materi(request, materi_id):
    materi = get_object_or_404(Materi, pk=materi_id)
    materi.delete()
    return redirect('course_list')
