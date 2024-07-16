# Import section.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.contrib.auth.decorators import login_required

# Create functions.
def index(request):
    """
    View for the index page, displaying the latest questions.
    
    :param HttpRequest request: The request object.
    :returns: The response with the rendered index page.
    :rtype: HttpResponse
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail_page(request, question_id):
    """
    View for the detail page, displaying a specific question and its choices.
    
    :param HttpRequest request: The request object.
    :param int question_id: The ID of the question to display.
    :returns: The response with the rendered detail page.
    :rtype: HttpResponse
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    """
    View for the results page, displaying the results of a specific question.
    
    :param HttpRequest request: The request object.
    :param int question_id: The ID of the question to display results for.
    :returns: The response with the rendered results page.
    :rtype: HttpResponse
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


@login_required
def vote(request, question_id):
    """
    Handles voting for a particular choice in a question.
    
    :param HttpRequest request: The request object.
    :param int question_id: The ID of the question being voted on.
    :returns: Redirects to the results page on successful vote.
    :rtype: HttpResponseRedirect
    :returns: The response with the rendered detail page if an error occurs.
    :rtype: HttpResponse
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form with an error message.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Redirect to the results page after successfully saving the vote.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
