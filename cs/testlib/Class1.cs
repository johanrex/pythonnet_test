using Yubico.YubiKey;

namespace testlib
{
    public class Class1
    {
        public int CountDevices()
        {
            var devices = YubiKeyDevice.FindAll();
            return devices.Count();
        }
    }
}