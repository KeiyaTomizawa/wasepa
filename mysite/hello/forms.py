# coding: utf-8
from django import forms


class HelloForm(forms.Form):
      your_name = forms.CharField(
          label='名前',
          max_length=20,
          required=True,
          widget=forms.TextInput()
      )

EMPTY_CHOICES = (
     ('', '-'*10),
)

NAME_CHOICES = (
     ('oomori', '大森'),
     ('shimizu', '清水'),
     ('tomizawa', '富澤'),

)

PLACE_CHOICES = (
       ('sagamigawa', '相模川'),
       ('misakiguchi', '三崎口')
)
class SampleForm(forms.Form):
    distance = forms.IntegerField(
        label='距離',
        min_value=1,
        max_value=20,
        required=True,
    )

    day = forms.DateField(
           label='日付',
           required=True,
           input_formats=[
               '%Y-%m-%d',  # 2010-01-01
               '%Y/%m/%d',  # 2010/01/01
           ]
    )

    time = forms.DateField(
           label='タイム',
           required=True,
           input_formats=[
               '%i-%s',  # 20-01
               '%i/%s',  # 20/01
           ]
    )

    send_message = forms.BooleanField(
          label='送信する',
          required=False,
    )

    name_r = forms.ChoiceField(
         label='名前',
        widget=forms.RadioSelect,
         choices=NAME_CHOICES,
         required=True,
    )

    name_s = forms.ChoiceField(
         label='名前',
         widget=forms.Select,
         choices=EMPTY_CHOICES + NAME_CHOICES,
         required=False,
    )

    place_r = forms.ChoiceField(
         label='場所',
        widget=forms.RadioSelect,
         choices=PLACE_CHOICES,
         required=True,
    )

    place_s = forms.ChoiceField(
         label='場所',
         widget=forms.Select,
         choices=EMPTY_CHOICES + PLACE_CHOICES,
         required=False,
    )
