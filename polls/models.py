# Import section.
from django.db import models
from django.utils import timezone
import datetime

# Create classes.

class Question(models.Model):
    """
    Represents a question in the poll application.
    
    :param str question_text: The text of the question.
    :param datetime pub_date: The date and time when the question was published.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """
        Returns a string representation of the Question.
        
        :returns: The text of the question.
        :rtype: str
        """
        return self.question_text

    def was_published_recently(self):
        """
        Determines if the question was published within the last day.
        
        :returns: True if the question was published within the last day, False otherwise.
        :rtype: bool
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # Admin options for displaying in the admin interface.
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    """
    Represents a choice related to a question in the poll application.
    
    :param Question question: The question this choice is associated with.
    :param str choice_text: The text of the choice.
    :param int votes: The number of votes this choice has received.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """
        Returns a string representation of the Choice.
        
        :returns: The text of the choice.
        :rtype: str
        """
        return self.choice_text