class CarRecord():
  def __init__(self, VehicleID, Registration, DateOfRegistration, EngineSize, PurchasePrice):
    self.VehicleID = VehicleID
    self.Registration = Registration
    self.DateOfRegistration = DateOfRegistration
    self.EngineSize = EngineSize
    self.PurchasePrice = PurchasePrice

Cars = [
  CarRecord(434, "Tom", "1/1/94", "V4", 987654),
  CarRecord(24, "Tob", "8/2/14", "V4", 98654),
  CarRecord(134, "Ton", "6/1/24", "V4", 12654),
  CarRecord(42, "Bob", "4/6/14", "V4", 98354),
  CarRecord(412, "Jer", "12/2/46", "V4", 7654),
]
