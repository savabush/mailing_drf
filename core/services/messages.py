

class MessageServices:

    @classmethod
    def validate_data(cls, serializer):
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.data
        return validated_data

    @classmethod
    def create(cls, validated_data, serializer):
        serializer.create(validated_data)

