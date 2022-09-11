from django.contrib.auth import login
import random
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from .forms import SignUpForm, SignupForm, GameChoice
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home/home.html')

class SignUp(View):
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            login(request, user)
            return redirect('home')

    def get(self, request):
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form':form})


class Signup(View):
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            # print(name)
            mail = form.cleaned_data['email']
            password = form.cleaned_data['password']
        else:
            return HttpResponse('try again')
        user = User.objects.create_user(name, mail, password)
        # user.save()
        login(request, user)
        return redirect('home')

    def get(self, request):
        form = SignupForm()
        return render(request, 'registration/signup2.html', {'form':form})


class game(View):
    Choices = ['Rock', 'Paper', 'Scissors']

    def get(self, request):
        form = GameChoice
        return render(request, 'home/game.html', {'form': form})

    def post(self, request):
        form = GameChoice(request.POST)
        if form.is_valid():
            man_choice = request.POST['player_choice']
            return HttpResponse(self.game(man_choice))


    def C_Choice(self):
        comp = random.choice(self.Choices)
        return comp

    def game(self, choice):

        raw_comp = (self.C_Choice())
        computer = (self.Choices.index(raw_comp))
        raw_man = choice
        raw_man = raw_man.capitalize()
        # print(f"computer chooses {raw_comp}")
        if raw_man in self.Choices:
            man = (self.Choices.index(raw_man))
            solver = man - computer
            solver = abs(solver)
            if solver == 1:
                var = {man: 'Man', computer: 'Computer'}
                k = var.get(max(var))
                return f"Computer chooses <b>{raw_comp}</b><br>{k} wins"
            elif solver == 2:
                var = {man: 'Man', computer: 'Computer'}
                k = var.get(min(var))
                return f"Computer chooses <b>{raw_comp}</b><br>{k} wins"
            else:
                return f"Computer chooses <b>{raw_comp}</b><br>It's a tie"

        else:
            print(f"You've chose wrongly, choice must be in {self.Choices}")
            return self.game(choice)



