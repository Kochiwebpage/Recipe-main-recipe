from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from Recipe_app.forms import FeedbackForm
from Recipe_app.models import Recipes, List, FoodType, UserProfile


def homefun(request):
    return render(request, 'Home.html')


def aboutfun(request):
    return render(request, 'about.html')


def recipefun(request):
    Rlist1 = request.GET.get('List')
    food_type = request.GET.get('FoodType')
    if Rlist1 is None:
        recipe = Recipes.objects.all()
    else:
        recipe = Recipes.objects.filter(Recipe__name=Rlist1)

    if food_type:
        recipe = recipe.filter(food_type__food_type=food_type)
    list1 = List.objects.all()
    food_types = FoodType.objects.all()
    dict1 = {'key1': list1, 'key2': recipe,'key4':food_types}
    return render(request, 'Recipe.html', dict1)


def details(request,pk):
    recipedetails = Recipes.objects.get(id=pk)
    dict2 = {'key3': recipedetails}
    return render(request, 'Details.html', dict2)


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        gender = request.POST['gender']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username taken')
                return redirect('signuppage')
            else:
                user = User.objects.create_user(username=username, first_name=first_name,last_name=last_name,email=email,password=password)
                UserProfile.objects.create(user=user, gender=gender)

                user.save();
                messages.success(request, 'Account created successfully. You are now logged in.')
                return redirect('loginpage')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('signuppage')
    return render(request, 'signup.html')


def loginfun(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            print("success")
        else:
            messages.info(request, "invalid username or password")
            return redirect('loginpage')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    messages.success(request,"Logged out Successfully")
    return redirect('loginpage')


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()

            subject = 'New Feedback Submission'
            message = f'Feedback from {form.cleaned_data["name"]}: {form.cleaned_data["feedback"]}'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.ADMIN_EMAIL]
            send_mail(subject, message, from_email, recipient_list)

            return redirect('feedback_success')  # Redirect to a success page
    else:
        form = FeedbackForm()

    return render(request, 'feedback_form.html', {'form': form})


def feedback_success(request):
    return render(request, 'feedback_success.html')





@login_required
def save_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipes, id=recipe_id)

    if request.user in recipe.saved_by.all():
        recipe.saved_by.remove(request.user)
    else:
        recipe.saved_by.add(request.user)

    return redirect('recipepage')



def saved_list(request):
    saved_recipes = Recipes.objects.filter(saved_by=request.user)
    return render(request, 'saved.html', {'saved_recipes': saved_recipes})



