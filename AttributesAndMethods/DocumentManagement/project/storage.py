from .topic import Topic
from .document import Document
from .category import Category

class Storage:
    def __init__(self):
        self.categories=[]
        self.documents=[]
        self.topics=[]
        self.category_ids={}
        self.topic_ids={}
        self.document_ids={}

    def add_category(self,category:Category):
        if category not in self.categories:
            self.categories.append(category)
            self.category_ids[category.id]=category
    def add_topic(self,topic:Topic) :
        if topic not in self.topics:
            self.topics.append(topic)
            self.topic_ids[topic.id]=topic
    def add_document(self,document:Document) :
        if document not in self.documents:
            self.documents.append(document)
            self.document_ids[document.id]=document

    def edit_category(self,category_id: int, new_name:str) :
        category=self.category_ids[category_id]
        category.name=new_name
        self.category_ids[category_id]=new_name
    def edit_topic(self,topic_id: int, new_topic: str, new_storage_folder: str) :
        topic=self.topic_ids[topic_id]
        topic.storage_folder=new_storage_folder
        topic.topic=new_topic
        self.topic_ids[topic_id]=new_topic
    def edit_document(self,document_id: int, new_file_name: str) :
        document=self.document_ids[document_id]
        document.file_name=new_file_name
    def delete_category(self,category_id):
        category = self.category_ids[category_id]
        del self.category_ids[category_id]
        self.categories.remove(category)
        del category
    def delete_topic(self,topic_id):
        topic = self.topic_ids[topic_id]
        del self.topic_ids[topic_id]
        self.topics.remove(topic)
        del topic
    def delete_document(self,document_id) :
        document = self.document_ids[document_id]
        del self.document_ids[document_id]
        self.documents.remove(document)
        del document
    def get_document(self,document_id):
        return self.document_ids[document_id]
    def __repr__(self):
        documents=list(map(str,self.documents))
        documents_categories=list(map(str,self.document_ids))
        documents_topics=list(map(str,self.document_ids))
        documents_file_names=list(map(str,self.document_ids))
        return "\n".join(documents)