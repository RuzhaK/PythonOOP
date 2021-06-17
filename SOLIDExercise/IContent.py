from abc import ABC, abstractmethod
class IContent(ABC):

    @abstractmethod
    def format(self,content):
        pass

#     @staticmethod
#     def myml_format(content):
#         return '\n'.join(['<myML>', content, '</myML>'])
#     @staticmethod
#     def basic_format(content):
#         return content.capitalize()
#     @staticmethod
#     def html_format(content):
#         return 'HTML'
#
# FORMAT_MAPPER = {'myml':IContent.myml_format,'html':IContent.html_format,'basic':IContent.basic_format}

class HTMLFormatter(IContent):
    def format(self,content):
        return f"<h1>{content}</h1>"
class MyMLFormatter(IContent):
    def format(self,content):
        return '\n'.join(['<myML>', content, '</myML>'])

class BasicFormatter(IContent):
    def format(self,content):
        return content.capitalize()

class Email:
    def __init__(self,content,formatter):
        self.content=formatter().format(content)


email=Email('abc',HTMLFormatter)
print(email.content)
