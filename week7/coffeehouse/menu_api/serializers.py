from rest_framework import serializers

from menu_api.models import Special, Ingredient

class SpecialSerializer(serializers.ModelSerializer):
    ingredients = serializers.HyperlinkedRelatedField(
        view_name="ingredient_detail_api_view",
        read_only=True,
        many=True,
    )
    calorie_count = serializers.ReadOnlyField()
    my_favorite = serializers.SerializerMethodField()

    def get_my_favorite(self, obj):
        return "THIS"
    class Meta:
        model = Special
        exclude = ('created_by',)
        
class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = '__all__'
