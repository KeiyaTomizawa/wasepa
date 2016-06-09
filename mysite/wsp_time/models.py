from __future__ import unicode_literals

from django.db import models

class Message(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
          return u"{0}:{1}... ".format(self.id, self.message[:10])

#class Posting(models.Model):
#       name = models.CharField(
#            max_length=64,
#         verbose_name='$BL>A0(B',
#          help_text='$B$"$J$?$NL>A0$rF~NO$7$F$/$@$5$$(B',
#       )
#     message = models.CharField(
#         max_length=255,
#          verbose_name='$B%a%C%;!<%8(B',
#           help_text='$B%a%C%;!<%8$rF~NO$7$F$/$@$5$$(B',
#        )
#     created_at = models.DateTimeField(
#            auto_now_add=True,
#         verbose_name='$BEPO?F|;~(B',
#      )
