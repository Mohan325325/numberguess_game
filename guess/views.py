from django.shortcuts import render , redirect
import random
from . models import session

player_name1=""
def home(request):
    if request.method == 'POST':
        global player_name1
        player_name1 = request.POST.get('player_name')
        return redirect('guess',player_name1)

    return render(request, 'guess/html/home.html')

def guess_num(request, player_name):
    if request.method == 'POST':
        global var
        secret_number = request.session.get('secret_number')
        guess = int(request.POST.get('guess'))
        attempts = request.session.get('attempts', 0)
        max_attempts = 10

        if guess == secret_number:
            message = f"Congratulations, {player_name1}! You guessed the correct number {secret_number} in {attempts} attempts."
            winner = session(player_name=player_name1,secret_number=secret_number,attempts=attempts,is_winner=True)
            winner.save()
            return render(request, 'guess/html/result.html', {'message': message, 'play_again': True})

        attempts += 1
        request.session['attempts'] = attempts

        if attempts >= max_attempts:
            message = f"Sorry, {player_name1}. You've run out of attempts. The correct number was {secret_number}."
            return render(request, 'guess/html/result.html', {'message': message, 'play_again': True})

        if guess < secret_number:
            feedback = "Too low. Try again."
        else:
            feedback = "Too high. Try again."

        return render(request, 'guess/html/guess_num.html', {'feedback': feedback, 'attempts': attempts, 'max_attempts': max_attempts})

def guess(request,player_name):
        request.session.clear()
        secret_number = random.randint(1, 100)
        request.session['secret_number'] = secret_number

        return render(request, 'guess/html/guess_num.html',{'player_name':player_name})
