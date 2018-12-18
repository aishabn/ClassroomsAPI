from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from classes.models import Classroom
from .serializers import ClassroomListSerializer, ClassroomDetailSerializer, ClassroomCreateUpdateSerializer

class ClassListView(ListAPIView):
	queryset= Classroom.objects.all()
	serializer_class = ClassroomListSerializer

class ClassDetailView(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class ClassUpdateView(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomCreateUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class ClassDeleteView(DestroyAPIView):
	queryset = Classroom.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class ClassCreateView(CreateAPIView):
	serializer_class = ClassroomCreateUpdateSerializer

	def perform_create(self, serializer):
		serializer.save(teacher=self.request.user)