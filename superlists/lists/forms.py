from django import forms
from lists.models import Item

EMPTY_LIST_ERROR = "You can't have an empty list item"  # 定制错误信息

# 这个类与该项目无关，仅为探索相关的API
class ItemFormAPI(forms.Form):
    item_text = forms.CharField(
        widget=forms.fields.TextInput(attrs={   # 设置表单的属性
            'placeholder': 'Enter a to-do item',
            'class': 'form-control input-lg',
        }),
    )

# ModelForm用于自动生成对应模型的表单
class ItemForm(forms.models.ModelForm):

    class Meta:
        model = Item    # 指定表单用于哪个模型
        fields = ('text',)
        widgets = {     # 设置表单属性
            'text': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
                'class': 'form-control input-lg',
            }),
        }
        error_messages = {  # 定制错误信息
            'text': {'required': EMPTY_LIST_ERROR}  # 重写要求非空的Field为空时的错误信息
        }