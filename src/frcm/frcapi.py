from frcm.datamodel.model import FireRiskPrediction, WeatherData
import frcm.fireriskmodel.compute


class FireRiskAPI:


    def compute(self, wd: WeatherData) -> FireRiskPrediction:

        return frcm.fireriskmodel.compute.compute(wd)




