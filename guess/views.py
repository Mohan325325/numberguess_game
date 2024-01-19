from django.shortcuts import render , redirect
import random
from . models import session

def home(request):
    if request.method == 'POST':
        player = request.POST.get('name')
        request.session['name'] = player
        return redirect('play_game')

    return render(request, 'guess/html/home.html')

def guess_num(request):
    if request.method == 'POST':
        secret_number = request.session.get('secret_number')
        guess = int(request.POST.get('guess'))
        attempts = request.session.get('attempts', 0)
        max_attempts = 10

        if guess == secret_number:
            message = f"Congratulations, {request.session.get('player_name')}! You guessed the correct number {secret_number} in {attempts} attempts."
            winner = session(secret_number=secret_number,attempts=attempts,is_winner=True)
            winner.save()
            return render(request, 'guess/html/result.html', {'message': message, 'play_again': True})

        attempts += 1
        request.session['attempts'] = attempts

        if attempts >= max_attempts:
            message = f"Sorry, {request.session.get('player_name')}. You've run out of attempts. The correct number was {secret_number}."
            return render(request, 'guess/html/result.html', {'message': message, 'play_again': True})

        if guess < secret_number:
            feedback = "Too low. Try again."
        else:
            feedback = "Too high. Try again."

        return render(request, 'guess/html/guess_num.html', {'feedback': feedback, 'attempts': attempts, 'max_attempts': max_attempts})

    else:
        # Clear session for a new user or a new game for an existing user
        request.session.clear()

        # Generate a new secret number for each new game
        secret_number = random.randint(1, 100)
        request.session['secret_number'] = secret_number

        return render(request, 'guess/html/guess_num.html')
