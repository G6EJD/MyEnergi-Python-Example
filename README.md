# MyEnergi-Python-Example
How to access and display MyEnergi data

Windows PC

1. Install a version of Python typically 3.10
2. The Python code here needs additional modules to be installed, so launch Windows Powershell(Admin)
3. Type:
4.     pip install requests
5.     pip install json
6. Repeat for other missing modules
7. Download the example Python code provided, to your desok top is easiest
8. Right click and edit with Idle
9. Edit the file to add your USername (HUB serial number) and Password
10. Choose Run
11. Enjoy

API Error Codes and meaning

CODE MEANING

0	O.K. / Success

-1	Invalid ID – The unit or group cannot be found or the user does not
have access rights to the ID.

-2	Invalid DSR command sequence number. Valid write values or 1-15
inclusive. Valid read values are 0-15 inclusive.

-3	No action taken. Command Sequence Number “csn” equals “err” for
single unit. i.e. Command Sequence number is same as last number
used.

-4	Hub not found. No associated hub record for the unit.

-5	Internal Error.

-6	Invalid load value.

-7	Year missing.

-8	Month missing or invalid.

-9	Day missing or invalid.

-10	Hour missing or invalid.

-11	Invalid TTL Value.

-12	User not authorised to perform operation.

-13	Serial No not found.

-14	Missing or bad parameter.

-15	Invalid password.

-16	New passwords don’t match.

-17	Invalid new password. Password must not contain “&”

-18	New password is same as old password.

-19	User not registered.

-20	Minute missing or invalid

-21	Slot missing or invalid

-22	Priority bad or missing

-23	Command not appropriate for device

-24	Check period bad or missing

-25	Min Green Level bad or missing

-26	Busy – Server is already sending a command to the device.

-27	Relay not fitted.

