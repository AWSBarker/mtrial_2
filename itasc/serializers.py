from rest_framework import serializers
from .models import Measurements

class MeasurementsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurements
        fields = ("measurements_timestamp" ,  "metadata_correlationid" , "metadata_receivedtime" ,
          "device_imei" , "measurements_annotations_irregularheartbeat" , "measurements_systolicbloodpressure_value",
          "measurements_diastolicbloodpressure_value" ,  "measurements_pulse_value")

#        fields = '__all__' #('metadata_correlationid','measurements_timestamp','device_imei') #, 'device_imsi') #'__all__'
#        fields = ('metadata_correlationid','measurements_timestamp','device_imei') #, 'device_imsi') #'__all__'

