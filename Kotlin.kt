open class SmartDevice(val name: String, val category: String) {

    var deviceStatus = "online"
         protected set
 
     open val deviceType = "unknown"
     open fun turnOn() {
          deviceStatus = "on"  
     }
     open fun turnOff() {
          deviceStatus = "off"
     }
 }
 
 class SmartLightDevice(deviceName: String, deviceCategory: String) :
     SmartDevice(name = deviceName, category = deviceCategory) {
     
         override val deviceType = "Smart Light"
         private var brightnessLevel = 0
         set(value) {
             if (value in 0..100) {
                 field = value
             }
         }
         override fun turnOn() {
             super.turnOn()
             brightnessLevel = 2
             println("$name turned on. The brightness level is $brightnessLevel.")
         }
         override fun turnOff() {
             super.turnOff()
             brightnessLevel = 0
             println("$name turned off")
            }
         fun increasebrightnessLevel() {
             brightnessLevel++
             println("Brightness Level increased to $brightnessLevel.")
         }
         fun decreasebrightnessLevel() {
             brightnessLevel--
             println("Brightness Level decreased to $brightnessLevel.")
         }
 }
 class SmartTvDevice(deviceName: String, deviceCategory: String) :
     SmartDevice(name = deviceName, category = deviceCategory) {
         
         override val deviceType = "Smart TV"
         private var speakerVolume = 2
         set(value) {
             if (value in 0..100) {
                 field = value
             }
         }
         private var channelNumber = 1
         set(value) {
             if (value in 0..200) {
                 field = value
             }
         }
         fun increaseSpeakerVolume() {
             speakerVolume++
             println("Speaker volume increased to $speakerVolume.")
         }
         fun decreaseSpeakerVolume() {
             speakerVolume--
             println("Speaker volume decreased to $speakerVolume.")
         }
         fun nextChannel() {
             channelNumber++
             println("Channel number increased to $channelNumber.")
         }
         fun previousChannel() {
             channelNumber--
             println("Channel number decreased to $channelNumber.")
         }
         override fun turnOn() {
             super.turnOn()
             println(
                 "$name is turned on. Speaker volume is set to $speakerVolume and channel number is " +
                     "set to $channelNumber."
             )
         }
         override fun turnOff() {
             super.turnOff()
             println(
                 "$name is turned off"
             )
         }
 }
     class SmartHome(
         val smartTvDevice: SmartTvDevice,
         val smartLightDevice: SmartLightDevice
     ) {
         var deviceTurnOnCount = 0
         private set
         fun turnOnTv() {
             deviceTurnOnCount++
             smartTvDevice.turnOn()
         }
         fun turnOffTv() {
             deviceTurnOnCount--
             smartTvDevice.turnOff()
         }
         
         fun increaseTvVolume() {
             smartTvDevice.increaseSpeakerVolume()
         }
         fun decreaseTvVolume() {
             smartTvDevice.decreaseSpeakerVolume()
         }
         fun changeTvChannelToNext() {
             smartTvDevice.nextChannel()
         }
         fun changeTvChannelToPrevious() {
             smartTvDevice.previousChannel()
         }
         fun turnOnLight() {
             deviceTurnOnCount++
             smartLightDevice.turnOn()
         }
 
         fun turnOffLight() {
             deviceTurnOnCount--
             smartLightDevice.turnOff()
         }
         fun increaseLightBrightness() {
             smartLightDevice.increasebrightnessLevel()
         }
         fun decreaseLightBrightness() {
             smartLightDevice.decreasebrightnessLevel()
         }
         fun turnOffAllDevices() {
         turnOffTv()
         turnOffLight()
         }
 }
 fun main() {
     var smartDevice: SmartDevice  = SmartTvDevice("AndroidTV", "Entertainment")
     smartDevice.turnOn()
     smartDevice = SmartLightDevice("Google Light", "Utility")
     smartDevice.turnOn()
 }