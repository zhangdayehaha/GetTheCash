# GetTheCash
PCI Express Base Specification, Rev. 4.0 Version 1.0
284
All timeout values specified for the Link Training and Status state machine (LTSSM) are minus 0
seconds and plus 50% unless explicitly stated otherwise. All timeout values must be set to the
specified values after Fundamental Reset. All counter values must be set to the specified values after
Fundamental Reset.
5 4.2.5.1 Detect
The purpose of this state is to detect when a far end termination is present. This state can be
entered at any time if directed.
4.2.5.2 Polling
The Port transmits training Ordered Sets and responds to the received training Ordered Sets. In
10 this state, bit lock and Symbol lock are established and Lane polarity is configured.
The polling state includes Polling.Compliance (see Section 4.2.6.2.2). This state is intended for use
with test equipment used to assess if the Transmitter and the interconnect present in the device
under test setup is compliant with the voltage and timing specifications in Table 8-3 and Table 8-11.
The Polling.Compliance state also includes a simplified inter-operability testing scheme that is
15 intended to be performed using a wide array of test and measurement equipment (i.e., pattern
generator, oscilloscope, BERT, etc.). This portion of the Polling.Compliance state is logically
entered by at least one component asserting the Compliance Receive bit (bit 4 in Symbol 5 of TS1)
while not asserting the Loopback bit (bit 2 in Symbol 5 of TS1) upon entering Polling.Active. The
ability to set the Compliance Receive bit is implementation specific. A provision for changing data
20 rates to that indicated by the highest common transmitted and received Data Rate Identifiers
(Symbol 4 of TS1) is also included to make this behavior scalable to various data rates.
IMPLEMENTATION NOTE
Use of Polling.Compliance
Polling.Compliance is intended for a compliance test environment and not entered during normal
25 operation and cannot be disabled for any reason. Polling.Compliance is entered based on the
physical system environment or configuration register access mechanism as described in
Section 4.2.6.2.1. Any other mechanism that causes a Transmitter to output the compliance pattern
is implementation specific and is beyond the scope of this specification.
4.2.5.3 Configuration
30 In Configuration, both the Transmitter and Receiver are sending and receiving data at the negotiated
data rate. The Lanes of a Port configure into a Link through a width and Lane negotiation
sequence. Also, Lane-to-Lane de-skew must occur, scrambling can be disabled if permitted, the
N_FTS is set, and the Disable or Loopback states can be entered.
PCI Express Base Specification, Rev. 4.0 Version 1.0
285
4.2.5.4 Recovery
In Recovery, both the Transmitter and Receiver are sending and receiving data using the configured
Link and Lane number as well as the previously supported data rate(s). Recovery allows a
configured Link to change the data rate of operation if desired, re-establish bit lock, Symbol lock or
5 Block alignment, and Lane-to-Lane de-skew. Recovery is also used to set a new N_FTS value and
enter the Loopback, Disabled, Hot Reset, and Configuration states.
4.2.5.5 L0
L0 is the normal operational state where data and control packets can be transmitted and received.
All power management states are entered from this state.
10 4.2.5.6 L0s
L0s is intended as a power savings state. When operating with separate reference clocks with
independent Spread Spectrum Clocking (SSC) (see Section 4.2.7), L0s is not supported and must not
be advertised in the capability registers. See Section 4.3.7.3 for a definition of SSC.
L0s allows a Link to quickly enter and recover from a power conservation state without going
15 through Recovery.
The entry to L0s occurs after receiving an EIOS.
The exit from L0s to L0 must re-establish bit lock, Symbol lock or Block alignment, and Lane-to-
Lane de-skew.
A Transmitter and Receiver Lane pair on a Port are not required to both be in L0s simultaneously.
20 4.2.5.7 L1
L1 is intended as a power savings state.
The L1 state allows an additional power savings over L0s at the cost of additional resume latency.
The entry to L1 occurs after being directed by the Data Link Layer and receiving an EIOS.
4.2.5.8 L2
25 Power can be aggressively conserved in L2. Most of the Transmitter and Receiver may be shut
off.50 Main power and clocks are not guaranteed, but Aux51 power is available.
When Beacon support is required by the associated system or form factor specification, an
Upstream Port that supports the wakeup capability must be able to send; and a Downstream Port
must be able to receive; a wakeup signal referred to as a Beacon.
30 The entry to L2 occurs after being directed by the Data Link Layer and receiving an EIOS.
50 The exception is the Receiver termination, which must remain in a low impedance state.
51 In this context, “Aux” power means a power source which can be used to drive the Beacon circuitry.
PCI Express Base Specification, Rev. 4.0 Version 1.0
286
4.2.5.9 Disabled
The intent of the Disabled state is to allow a configured Link to be disabled until directed or
Electrical Idle is exited (i.e., due to a hot removal and insertion) after entering Disabled.
Disabled uses bit 1 (Disable Link) in the Training Control field (see Table 4-5 and Table 4-6) which
5 is sent within the TS1 and TS2 Ordered Sets.
A Link can enter Disabled if directed by a higher Layer. A Link can also reach the Disabled state by
receiving two consecutive TS1 Ordered Sets with the Disable Link bit asserted (see
Sections 4.2.6.3.1 and 4.2.6.4.5).
4.2.5.10Loopback
10 Loopback is intended for test and fault isolation use. Only the entry and exit behavior is specified,
all other details are implementation specific. Loopback can operate on either a per-Lane or
configured Link basis.
A loopback master is the component requesting Loopback.
A loopback slave is the component looping back the data.
15 Loopback uses bit 2 (Loopback) in the Training Control field (see Table 4-5 and Table 4-6) which is
sent within the TS1 and TS2 Ordered Sets.
The entry mechanism for a loopback master is device specific.
The loopback slave device enters Loopback whenever two consecutive TS1 Ordered Sets are
received with the Loopback bit set.
20 IMPLEMENTATION NOTE
Use of Loopback
Once in the Loopback state, the master can send any pattern of Symbols as long as the encoding
rules are followed. Once in Loopback, the concept of data scrambling is no longer relevant; what is
sent out is looped back. The mechanism(s) and/or interface(s) utilized by the Data Link Layer to
25 notify the Physical Layer to enter the Loopback state is component implementation specific and
beyond the scope of this specification.
4.2.5.11Hot Reset
Hot Reset uses bit 0 (Hot Reset) in the Training Control field (see Table 4-5 and Table 4-6) within
the TS1 and TS2 Ordered Sets.
30 A Link can enter Hot Reset if directed by a higher Layer. A Link can also reach the Hot Reset state
by receiving two consecutive TS1 Ordered Sets with the Hot Reset bit asserted (see
Section 4.2.6.11).
PCI Express Base Specification, Rev. 4.0 Version 1.0
287
4.2.6 Link Training and Status State Rules
Various Link status bits are monitored through software with the exception of LinkUp which is
monitored by the Data Link Layer. Table 4-15 describes how the Link status bits must be handled
throughout the LTSSM (for more information, see Section 3.2 for LinkUp; Section 7.5.3.8 for Link
Speed, Link Width, and Link Training; Section 6.2 for Receiver Error; 5 and Section 6.7 for In-Band
Presence). A Receiver may also optionally report an 8b/10b Error in the Lane Error Status register
when operating in 8b/10b encoding, when allowed to report the error as a Receiver Error in
Table 4-15.
IMPLEMENTATION NOTE
10 Receiver Errors During Configuration and Recovery States
Allowing Receiver Errors to be set while in Configuration or Recovery is intended to allow
implementations to report Link Errors that occur while processing packets in those states. For
example, if the LTSSM transitions from L0 to Recovery while a TLP is being received, a Link Error
that occurs after the LTSSM transition can be reported.
15 Table 4-15: Link Status Mapped to the LTSSM
LTSSM State Link
Width Link Speed LinkUp Link
Training Receiver Error
In-Band
Presence
52
Detect Undefined Undefined 0b 0b No action 0b
Polling Undefined Set to 2.5 GT/s on
entry from Detect.
Link speed may
change on entry to
Polling.Compliance
.
0b 0b No action 1b
Configuration Set No action 0b/1b
53
1b Set on 8b/10b
Error.
Optional: Set on
Link Error when
using 128b/130b
encoding.
1b
Recovery No action Set to new speed
when speed
changes
1b 1b Optionally set
on Link Error.
1b
L0 No action No action 1b 0b Set on Link
Error.
1b
L0s No action No action 1b 0b No action 1b
52 In-band refers to the fact that no sideband signals are used to calculate the presence of a powered up device on
the other end of a Link.
53 LinkUp will always be 0 if coming into Configuration via Detect -> Polling -> Configuration and LinkUp will always
be 1 if coming into Configuration from any other state.
PCI Express Base Specification, Rev. 4.0 Version 1.0
288
LTSSM State Link
Width Link Speed LinkUp Link
Training Receiver Error
In-Band
Presence
52
L1 No action No action 1b 0b No action 1b
L2 No action No action 1b 0b No action 1b
Disabled Undefined Undefined 0b 0b Optional:
Set on 8b/10b
Error
1b
Loopback No action Link speed may
change on entry to
Loopback from
Configuration.
0b 0b No action 1b
Hot Reset No action No action 0b 0b Optional:
Set on 8b/10b
Error
1b
The state machine rules for configuring and operating a PCI Express Link are defined in the
following sections.
Figure 4-23: Main State Diagram for Link Training 5 and Status State Machine
4.2.6.1 Detect
The Detect substate machine is shown in Figure 4-24.
OM13800B
Detect
Polling
Configuration
L0
Disabled
Hot Reset
Loopback
Recovery
L0s
L2
L1
Initial State or
Directed by
Data Link Layer
PCI Express Base Specification, Rev. 4.0 Version 1.0
289
4.2.6.1.1 Detect.Quiet
 Transmitter is in an Electrical Idle state.
o The DC common mode voltage is not required to be within specification.
 2.5 GT/s data rate is selected as the frequency of operation. If the frequency of operation was
5 not 2.5 GT/s data rate on entry to this substate, the LTSSM must stay in this substate for at least
1 ms, during which the frequency of operation must be changed to the 2.5 GT/s data rate.
o Note: This does not affect the advertised data rate in the TS1 and TS2 Ordered Sets.
 All Receivers must meet the the ZRX-DC specification for 2.5 GT/s within 1ms (see Table 8-11) of
entering this substate. The LTSSM must stay in this substate until the ZRX-DC specification for
10 2.5 GT/s is met.
 LinkUp = 0b (status is cleared).
 The Equalization 8.0 GT/s Phase 1 Successful, Equalization 8.0 GT/s Phase 2 Successful,
Equalization 8.0 GT/s Phase 3 Successful, and Equalization 8.0 GT/s Complete bits of the Link
Status 2 register are all set to 0b. The Equalization 16.0 GT/s Phase 1 Successful, Equalization
15 16.0 GT/s Phase 2 Successful, Equalization 16.0 GT/s Phase 3 Successful and Equalization 16.0
GT/s Complete bits of the 16.0 GT/s Status register are all set to 0b.
 The directed_speed_change variable is reset to 0b. The upconfigure_capable variable is reset to
0b. The idle_to_rlock_transitioned variable is reset to 00h. The select_deemphasis variable
must be set to either 0b or 1b based on platform specific needs for an Upstream Port and
20 identical to the Selectable Preset/De-emphasis field in the Link Control 2 register for a
Downstream Port. The equalization_done_8GT_data_rate and
equalization_done_16GT_data_rate variables are reset to 0b.
o Note that since these variables are defined with the 2.0 specification, pre-2.0 devices
would not implement these variables and will always take the path as if the
25 directed_speed_change and upconfigure_capable variables are constantly reset to 0b and
the idle_to_rlock_transitioned variable is constantly set to FFh.
 The next state is Detect.Active after a 12 ms timeout or if Electrical Idle is broken on any Lane.
4.2.6.1.2 Detect.Active
 The Transmitter performs a Receiver Detection sequence on all un-configured Lanes that can
30 form one or more Links (see Section 8.4.5.7 for more information).
 Next state is Polling if a Receiver is detected on all unconfigured Lanes.
 Next state is Detect.Quiet if a Receiver is not detected on any Lane.
 If at least one but not all un-configured Lanes detect a Receiver, then:
1. Wait for 12 ms.
35 2. The Transmitter performs a Receiver Detection sequence on all un-configured Lanes that
can form one or more Links (see Section 8.4.5.7 for more information),
PCI Express Base Specification, Rev. 4.0 Version 1.0
290
o The next state is Polling if exactly the same Lanes detect a Receiver as the first Receiver
Detection sequence.
 Lanes that did not detect a Receiver must:
i) Be associated with a new LTSSM if this optional feature is supported.
5 or
ii) All Lanes that cannot be associated with an optional new LTSSM must transition
to Electrical Idle.54
• These Lanes must be re-associated with the LTSSM immediately after the
LTSSM in progress transitions back to Detect.
10 • An EIOS does not need to be sent before transitioning to Electrical Idle.
o Otherwise, the next state is Detect.Quiet.
Figure 4-24: Detect Substate Machine
4.2.6.2 Polling
15 The Polling substate machine is shown in Figure 4-25.
4.2.6.2.1 Polling.Active
 Transmitter sends TS1 Ordered Sets with Lane and Link numbers set to PAD on all Lanes that
detected a Receiver during Detect.
o The Data Rate Identifier Symbol of the TS1 Ordered Sets must advertise all data rates
20 that the Port supports, including those that it does not intend to use.
o The Transmitter must wait for its TX common mode to settle before exiting from
Electrical Idle and transmitting the TS1 Ordered Sets.
 The Transmitter must drive patterns in the default voltage level of the Transmit
Margin field within 192 ns from entry to this state. This transmit voltage level
25 will remain in effect until Polling.Compliance or Recovery.RcvrLock is entered.
54 The common mode being driven is not required to meet the Absolute Delta Between DC Common Mode During L0
and Electrical Idle (VTX-CM-DC-ACTIVE-IDLE-DELTA) specification (see Table 8-7).
PCI Express Base Specification, Rev. 4.0 Version 1.0
291
Next state is Polling.Compliance if the Enter Compliance bit (bit  4) in the Link Control 2
register is 1b. If the Enter Compliance bit was set prior to entry to Polling.Active, the transition
to Polling.Compliance must be immediate without sending any TS1 Ordered Sets.
 Next state is Polling.Configuration after at least 1024 TS1 Ordered Sets were transmitted, and all
5 Lanes that detected a Receiver during Detect receive eight consecutive training sequences (or
their complement) satisfying any of the following conditions:
o TS1 with Lane and Link numbers set to PAD and the Compliance Receive bit (bit 4 of
Symbol 5) is 0b.
o TS1 with Lane and Link numbers set to PAD and the Loopback bit (bit 2 of Symbol 5)
10 is 1b.
o TS2 with Lane and Link numbers set to PAD.
 Otherwise, after a 24 ms timeout the next state is:
o Polling.Configuration if,
(i) Any Lane, which detected a Receiver during Detect, received eight consecutive training
15 sequences (or their complement) satisfying any of the following conditions:
1. TS1 with Lane and Link numbers set to PAD and the Compliance Receive bit (bit 4
of Symbol 5) is 0b.
2. TS1 with Lane and Link numbers set to PAD and the Loopback bit (bit 2 of Symbol
5) is 1b.
20 3. TS2 with Lane and Link numbers set to PAD.
and a minimum of 1024 TS1 Ordered Sets are transmitted after receiving one TS1 or
TS2 Ordered Set55.
And
(ii) At least a predetermined set of Lanes that detected a Receiver during Detect have
25 detected an exit from Electrical Idle at least once since entering Polling.Active.
 Note: This may prevent one or more bad Receivers or Transmitters from
holding up a valid Link from being configured, and allow for additional training
in Polling.Configuration. The exact set of predetermined Lanes is
implementation specific. Note that up to the 1.1 specification this
30 predetermined set was equal to the total set of Lanes that detected a Receiver.
 Note: Any Lane that receives eight consecutive TS1 or TS2 Ordered Sets should
have detected an exit from Electrical Idle at least once since entering
Polling.Active.
o Else Polling.Compliance if either (a) or (b) is true:
35 (a) not all Lanes from the predetermined set of Lanes from (ii) above have detected an exit
from Electrical Idle since entering Polling.Active.
55 Earlier versions of this specification required transmission of 1024 TS1 Ordered Sets after receiving one TS1
Ordered Set. This behavior is still permitted but the implementation will be more robust if it follows the behavior of
transmitting 1024 TS1 Ordered Sets after receiving one TS1 or TS2 Ordered Set.
PCI Express Base Specification, Rev. 4.0 Version 1.0
292
(b) any Lane that detected a Receiver during Detect received eight consecutive TS1 Ordered
Sets (or their complement) with the Lane and Link numbers set to PAD, the Compliance
Receive bit (bit 4 of Symbol 5) is 1b, and the Loopback bit (bit 2 of Symbol 5) is 0b.
 Note: If a passive test load is applied on all Lanes then the device will go to
5 Polling.Compliance.
o Else Detect if the conditions to transition to Polling.Configuration or
Polling.Compliance are not met
PCI Express Base Specification, Rev. 4.0 Version 1.0
293
4.2.6.2.2 Polling.Compliance
 The Transmit Margin field of the Link Control 2 register is sampled on entry to this substate and
becomes effective on the transmit package pins within 192 ns of entry to this substate and
remain effective through the time the LTSSM is in this substate.
5  The data rate and de-emphasis level for transmitting the compliance pattern are determined on
the transition from Polling.Active to Polling.Compliance using the following algorithm.
o If the Port is capable of transmitting at the 2.5 GT/s data rate only, the data rate for
transmitting the compliance pattern is 2.5 GT/s and the de-emphasis level is -3.5 dB.
o Else if the Port entered Polling.Compliance due to detecting eight consecutive TS1
10 Ordered Sets in Polling.Active with the Compliance Receive bit (bit 4 of Symbol 5)
asserted and the Loopback bit (bit 2 of Symbol 5) deasserted then the data rate for
transmission is that indicated by the highest common transmitted and received Data
Rate Identifiers (Symbol 4 of the TS1 sequence) advertised on the eight consecutive TS1
Ordered Sets received on any Lane that detected a Receiver during Detect. The
15 select_deemphasis variable must be set equal to the Selectable De-emphasis bit (Symbol
4 bit 6) in the eight consecutive TS1 Ordered Sets it received in Polling.Active substate.
If the common data rate is 8.0 GT/s or higher, the select_preset variable on each Lane is
set to the Transmitter preset value advertised in the Transmitter Preset field of the eight
consecutive EQ TS1 Ordered Sets on the corresponding Lane , provided the value is not
20 a Reserved encoding, and this value must be used by the transmitter (for 8.0 GT/s Data
Rate, use of the Receiver preset hint value advertised in those eight consecutive EQ TS1
Ordered Sets is optional). If the common Data Rate is 8.0 GT/s or higher, any Lanes
that did not receive eight consecutive EQ TS1 Ordered Sets with Transmitter preset
information, or that received a value for a Reserved encoding, can use any supported
25 Transmitter preset in an implementation specific manner.
o Else if the Enter Compliance bit in the Link Control 2 register is 1b, the data rate for
transmitting the compliance pattern is defined by the Target Link Speed field in the Link
Control 2 register. The select_deemphasis variable is Set when the Compliance
Preset/De-emphasis field in the Link Control 2 register equals 0001b if the data rate will
30 be 5.0 GT/s. If the data rate will be 8.0 GT/s or higher, the select_preset variable on
each Lane is set to, and the transmitter must operate with, the preset value provided in
the Compliance Preset/De-emphasis Value (bits 15:12) in the Link Control 2 register
provided the value is not a Reserved encoding.
o Else the data rate, preset, and de-emphasis level settings are defined as follows based on
35 the component’s maximum supported data rate and the number of times
Polling.Compliance has been entered with this entry criteria:
Setting #1: Data Rate = 2.5 GT/s, De-emphasis Level = -3.5 dB
Setting #2: Data Rate = 5.0 GT/s, De-emphasis Level = -3.5 dB
Setting #3: Data Rate = 5.0 GT/s, De-emphasis Level = -6 dB
40 Setting #4: Data Rate = 8.0 GT/s, with Transmitter Preset Encoding 0000b defined in
Section 4.2.3.2
PCI Express Base Specification, Rev. 4.0 Version 1.0
294
Setting #5: Data Rate = 8.0 GT/s, with Transmitter Preset Encoding 0001b defined in
Section 4.2.3.2
Setting #6: Data Rate = 8.0 GT/s, with Transmitter Preset Encoding 0010b defined in
Section 4.2.3.2
Setting #7: Data Rate = 8.0 GT/s, with Transmitter Preset 5 Encoding 0011b defined in
Section 4.2.3.2
Setting #8: Data Rate = 8.0 GT/s, with Transmitter Preset Encoding 0100b defined in
Section 4.2.3.2
Setting #9: Data Rate = 8.0 GT/s, with Transmitter Preset Encoding 0101b defined in
10 Section 4.2.3.2
Setting #10: Data Rate = 8.0 GT/s, with Transmitter Preset Encoding 0110b defined in
Section 4.2.3.2
Setting #11: Data Rate = 8.0 GT/s, with Transmitter Preset Encoding 0111b defined in
Section 4.2.3.2
15 Setting #12: Data Rate = 8.0 GT/s, with Transmitter Preset Encoding 1000b defined in
Section 4.2.3.2
Setting #13: Data Rate = 8.0 GT/s, with Transmitter Preset Encoding 1001b defined in
Section 4.2.3.2
Setting #14: Data Rate = 8.0 GT/s, with Transmitter Preset Encoding 1010b defined in
20 Section 4.2.3.2
Setting #15: Data Rate = 16.0 GT/s, with Transmitter Preset Encoding 0000b defined in
Section 4.2.3.2
Setting #16: Data Rate = 16.0 GT/s, with Transmitter Preset Encoding 0001b defined in
Section 4.2.3.2
25 Setting #17: Data Rate = 16.0 GT/s, with Transmitter Preset Encoding 0010b defined in
Section 4.2.3.2
Setting #18: Data Rate = 16.0 GT/s, with Transmitter Preset Encoding 0011b defined in
Section 4.2.3.2
Setting #19: Data Rate = 16.0 GT/s, with Transmitter Preset Encoding 0100b defined in
30 Section 4.2.3.2
Setting #20: Data Rate = 16.0 GT/s, with Transmitter Preset Encoding 0101b defined in
Section 4.2.3.2
Setting #21: Data Rate = 16.0 GT/s, with Transmitter Preset Encoding 0110b defined in
Section 4.2.3.2
35 Setting #22: Data Rate = 16.0 GT/s, with Transmitter Preset Encoding 0111b defined in
Section 4.2.3.2
Setting #23: Data Rate = 16.0 GT/s, with Transmitter Preset Encoding 1000b defined in
Section 4.2.3.2
PCI Express Base Specification, Rev. 4.0 Version 1.0
295
Setting #24: Data Rate = 16.0 GT/s, with Transmitter Preset Encoding 1001b defined in
Section 4.2.3.2
Setting #25: Data Rate = 16.0 GT/s, with Transmitter Preset Encoding 1010b defined in
Section 4.2.3.2
Settings #26 to #34: Data Rate = 16.0 GT/s, with Transmitter 5 Preset Encoding 0100b
defined in Section 4.2.3.2.
Subsequent entries to Polling.Compliance repeat the above sequence. For example, the state
sequence which causes a Port to transmit the Compliance pattern at a data rate of 5.0 GT/s
and a de-emphasis level of -6 dB is: Polling.Active, Polling.Compliance (2.5 GT/s and -3.5
10 dB), Polling.Active, Polling.Compliance (5.0 GT/s and -3.5 dB), Polling.Active,
Polling.Compliance (5.0 GT/s and -6 dB).
The sequence must be set to Setting #1 in the Polling.Configuration state if the Port
supports 16.0 GT/s or higher Data Rates, or the Port’s Receivers do not meet the ZRX-DC
specification for 2.5 GT/s when they are operating at 8.0 GT/s or higher data rates (see
15 Table 8-11). All Ports are permitted to set the sequence to Setting #1 in the
Polling.Configuration state.
PCI Express Base Specification, Rev. 4.0 Version 1.0
296
IMPLEMENTATION NOTE
Compliance Load Board Usage to Generate Compliance Patterns
It is envisioned that the compliance load (base) board may send a 100 MHz signal for about 1 ms on
one leg of a differential pair at 350 mV peak-to-peak on any Lane to cycle the device to the desired
speed and de-emphasis level. The device under test is required, b 5 ased on its maximum supported
data rate, to cycle through the following settings in order, for each entry to Polling.Compliance from
Polling.Active, starting with the first setting on the first entry to Polling.Compliance after the
Fundamental Reset:
 Data Rate = 2.5 GT/s, De-emphasis Level = -3.5 dB
10  Data Rate = 5.0 GT/s, De-emphasis Level = -3.5 dB
 Data Rate = 5.0 GT/s, De-emphasis Level = -6 dB
 Data Rate = 8.0 GT/s, with Transmitter Preset Encoding 0000b defined in Section 4.2.3.2
 Data Rate = 8.0 GT/s, with Transmitter Preset Encoding 0001b defined in Section 4.2.3.2
 Data Rate = 8.0 GT/s, with Transmitter Preset Encoding 0010b defined in Section 4.2.3.2
15  Data Rate = 8.0 GT/s, with Transmitter Preset Encoding 0011b defined in Section 4.2.3.2
 Data Rate = 8.0 GT/s, with Transmitter Preset Encoding 0100b defined in Section 4.2.3.2
 Data Rate = 8.0 GT/s, with Transmitter Preset Encoding 0101b defined in Section 4.2.3.2
 Data Rate = 8.0 GT/s, with Transmitter Preset Encoding 0110b defined in Section 4.2.3.2
 Data Rate = 8.0 GT/s, with Transmitter Preset Encoding 0111b defined in Section 4.2.3.2
20  Data Rate = 8.0 GT/s, with Transmitter Preset Encoding 1000b defined in Section 4.2.3.2
 Data Rate = 8.0 GT/s, with Transmitter Preset Encoding 1001b defined in Section 4.2.3.2
 Data Rate = 8.0 GT/s, with Transmitter Preset Encoding 1010b defined in Section 4.2.3.2
 Data Rate = 16.0 GT/s, with Transmitter Preset Encoding 0000b defined in Section 4.2.3.2
 Data Rate = 16.0 GT/s, with Transmitter Preset Encoding 0001b defined in Section 4.2.3.2
25  Data Rate = 16.0 GT/s, with Transmitter Preset Encoding 0010b defined in Section 4.2.3.2
 Data Rate = 16.0 GT/s, with Transmitter Preset Encoding 0011b defined in Section 4.2.3.2
 Data Rate = 16.0 GT/s, with Transmitter Preset Encoding 0100b defined in Section 4.2.3.2
 Data Rate = 16.0 GT/s, with Transmitter Preset Encoding 0101b defined in Section 4.2.3.2
 Data Rate = 16.0 GT/s, with Transmitter Preset Encoding 0110b defined in Section 4.2.3.2
30  Data Rate = 16.0 GT/s, with Transmitter Preset Encoding 0111b defined in Section 4.2.3.2
 Data Rate = 16.0 GT/s, with Transmitter Preset Encoding 1000b defined in Section 4.2.3.2
 Data Rate = 16.0 GT/s, with Transmitter Preset Encoding 1001b defined in Section 4.2.3.2
 Data Rate = 16.0 GT/s, with Transmitter Preset Encoding 1010b defined in Section 4.2.3.2
 Nine instances of Data Rate = 16.0 GT/s, with Transmitter Preset Encoding 0100b defined in
35 Section 4.2.3.2.
 If the compliance pattern data rate is not 2.5 GT/s and any TS1 Ordered Sets were transmitted
in Polling.Active prior to entering Polling.Compliance, the Transmitter sends either one EIOS
or two consecutive EIOSs prior to entering Electrical Idle. If the compliance pattern data rate is
40 not 2.5 GT/s and TS1 Ordered Sets were not transmitted in Polling.Active prior to entering
PCI Express Base Specification, Rev. 4.0 Version 1.0
297
Polling.Compliance, the Transmitter must enter Electrical Idle without transmitting any EIOSs.
During the period of Electrical Idle, the data rate is changed to the new speed and stabilized. If
the frequency of operation will be 5.0 GT/s, the de-emphasis/preset level must be set to -3.5 dB
if the select_deemphasis variable is 1b else it must be set to -6 dB. If the frequency of operation
will be 8.0 GT/s or higher, the Transmitter preset value must be 5 set to the value in the
select_preset variable. The period of Electrical Idle is greater than 1 ms but it is not to exceed
2 ms.
 Behavior during Polling Compliance after the data rate and de-emphasis/preset level are
determined must follow the following rules:
10 o If the Port entered Polling.Compliance due to detecting eight consecutive TS1 Ordered
Sets in Polling.Active with the Compliance Receive bit (bit 4 of Symbol 5) asserted and
the Loopback bit (bit 2 of Symbol 5) deasserted or both the Enter Compliance bit and
the Enter Modified Compliance bit in the Link Control 2 register are set to 1b then the
Transmitter sends out the Modified Compliance Pattern (see Section 4.2.9) at the above
15 determined data rate with the error status Symbol set to all 0’s on all Lanes that detected
a Receiver during Detect.
 If the data rate is 2.5 GT/s or 5.0 GT/s, a particular Lane’s Receiver
independently signifies a successful lock to the incoming Modified Compliance
Pattern by looking for any one occurrence of the Modified Compliance Pattern
20 and then setting the Pattern Lock bit (bit 8 of the 8 bit error status Symbol) in
the same Lane of its own transmitted Modified Compliance Pattern.
• The error status Symbols are not to be used for the lock process since
they are undefined at any given moment.
• An occurrence is defined above as the following sequence of 8b/10b
25 Symbols; K28.5, D21.5, K28.5, and D10.2 or the complement of each of
the individual Symbols.
• The device under test must set the Pattern Lock bit of the Modified
Compliance Pattern it transmits at the Transmitter package pin(s) after
successfully locking to the incoming Modified Compliance Pattern within
30 1 ms of receiving the Modified Compliance Pattern at its Receiver
package pin(s).
 If the data rate is 8.0 GT/s or higher: The Error_Status field is set to 00h on
entry to this substate. Each Lane sets the Pattern Lock bit independently when it
achieves Block Alignment as described in Section 4.2.2.2.1. After Pattern Lock is
35 achieved, Symbols received in Data Blocks are compared to the Idle data Symbol
(00h) and each mismatched Symbol causes the Receiver Error Count field to be
incremented by 1. The Receiver Error Count saturates at 127 (further
mismatched Symbols do not change the Receiver Error Count). The Pattern
Lock and Receiver Error Count information for each Lane is transmitted as part
40 of the SKP Ordered Sets transmitted in that Lane's Modified Compliance
Pattern. See Section 4.2.7 for more information. The device under test must set
the Pattern Lock bit in the SKP Ordered Set it transmits within 4 ms of receiving
the Modified Compliance Pattern at its Receiver package pin(s).
PCI Express Base Specification, Rev. 4.0 Version 1.0
298
The scrambling requirements defined in Section 4.2.2.4 are applied to the received
Modified Compliance Pattern. For example, the scrambling LFSR seed is set per Lane,
an EIEOS initializes the LFSR and SKP Ordered Sets do not advance the LFSR.
IMPLEMENTATION NOTE
5 Handling Bit Slip and Block Alignment
Devices should ensure that their Receivers have stabilized before attempting to obtain Block
alignment and signaling Pattern Lock. For example, if an implementation expects to see bit slips in
the initial few bits, it should wait for that time to be over before settling on a Block Alignment.
Devices may also want to revalidate their Block alignment prior to setting the Pattern Lock bit.
10  If the data rate is 2.5 GT/s or 5.0 GT/s, once a particular Lane indicates it has
locked to the incoming Modified Compliance Pattern the Receiver Error Count
for that particular Lane is incremented every time a Receiver error occurs.
• The error status Symbol uses the lower 7 bits as the Receiver Error
Count field and this field will remain stuck at all 1’s if the count reaches
15 127.
• The Receiver must not make any assumption about the 10-bit patterns it
will receive when in this substate if 8b/10b encoding is used.
 If the Enter Compliance bit in the Link Control 2 register is 0b, the next state is
Detect if directed
20  Else if the Enter Compliance bit was set to 1b on entry to Polling.Compliance,
next state is Polling.Active if any of the following conditions apply:
• The Enter Compliance bit in the Link Control 2 register has changed to
0b
• The Port is an Upstream Port and an EIOS is received on any Lane. The
25 Enter Compliance bit is reset to 0b when this condition is true.
If the Transmitter was transmitting at a data rate other than 2.5 GT/s, or the
Enter Compliance bit in the Link Control 2 register was set to 1b during entry to
Polling.Compliance, the Transmitter sends eight consecutive EIOS and enters
Electrical Idle prior to transitioning to Polling.Active. During the period of
30 Electrical Idle, the data rate is changed to 2.5 GT/s and stabilized and the deemphasis
level is set to -3.5 dB. The period of Electrical Idle is greater than 1 ms
but must not exceed 2 ms.
 Note: Sending multiple EIOS provides enough robustness such that the other
Port detects at least one EIOS and exits Polling.Compliance substate when the
35 configuration register mechanism was used for entry.
o Else if the Port entered Polling.Compliance due to the Enter Compliance bit of the Link
Control 2 register being set to 1b and the Enter Modified Compliance bit of the Link
Control 2 register being set to 0b:
PCI Express Base Specification, Rev. 4.0 Version 1.0
299
(a) Transmitter sends out the compliance pattern on all Lanes that detected a Receiver
during Detect at the data rate and de-emphasis/preset level determined above.
(b) Next state is Polling.Active if any of the following two conditions are true:
1.. The Enter Compliance bit in the Link Control 2 register has changed to 0b (from 1b)
since entering 5 Polling.Compliance.
2.. The Port is an Upstream Port, the Enter Compliance bit in the Link Control 2
register is set to 1b and an EIOS has been detected on any Lane. The Enter
Compliance bit is reset to 0b when this condition is true.
The Transmitter sends eight consecutive EIOSs and enters Electrical Idle prior to
10 transitioning to Polling.Active. During the period of Electrical Idle, the data rate is
changed to 2.5 GT/s and stabilized. The period of Electrical Idle is greater than 1 ms
but must not exceed 2 ms.
Note: Sending multiple EIOSs provides enough robustness such that the other Port
detects at least one EIOS and exits Polling.
15 o Else:
(a) Transmitter sends out the following patterns on Lanes that detected a Receiver during
Detect at the data rate and de-emphasis/preset level determined above:
 For Settings #1 to #25: Compliance pattern on all Lanes.
 For Setting #26: Jitter Measurement Pattern on all Lanes.
20  For Setting #27: Jitter Measurement Pattern on Lanes 0/8/16/24 and
Compliance pattern on all other Lanes.
 For Setting #28: Jitter Measurement Pattern on Lanes 1/9/17/25 and
Compliance pattern on all other Lanes.
 For Setting #29: Jitter Measurement Pattern on Lanes 2/10/18/26 and
25 Compliance pattern on all other Lanes.
 For Setting #30: Jitter Measurement Pattern on Lanes 3/11/19/27 and
Compliance patter on all other Lanes.
 For Setting #31: Jitter Measurement Pattern on Lanes 4/12/20/28 and
Compliance pattern on all other Lanes.
30  For Setting #32: Jitter Measurement Pattern on Lanes 5/13/21/29 and
Compliance pattern on all other Lanes.
 For Setting #33: Jitter Measurement Pattern on Lanes 6/14/22/30 and
Compliance pattern on all other Lanes.
 For Setting #34: Jitter Measurement Pattern on Lanes 7/15/23/31 and
35 Compliance pattern on all other Lanes.
(b) Next state is Polling.Active if an exit of Electrical Idle is detected at the Receiver of any
Lane that detected a Receiver during Detect.
If the Transmitter is transmitting at a data rate other than 2.5 GT/s, the Transmitter
sends eight consecutive EIOSs and enters Electrical Idle prior to transitioning to
PCI Express Base Specification, Rev. 4.0 Version 1.0
300
Polling.Active. During the period of Electrical Idle, the data rate is changed to 2.5 GT/s
and stabilized. The period of Electrical Idle is greater than 1 ms but must not exceed
2 ms.
4.2.6.2.3 Polling.Configuration
5  Receiver must invert polarity if necessary (see Section 4.2.4.4).
 The Transmit Margin field of the Link Control 2 register must be reset to 000b on entry to this
substate.
 The Transmitter’s Polling.Compliance sequence setting is updated, if required, as described in
Section 4.2.6.2.2.
10  Transmitter sends TS2 Ordered Sets with Link and Lane numbers set to PAD on all Lanes that
detected a Receiver during Detect.
o The Data Rate Identifier Symbol of the TS2 Ordered Sets must advertise all data rates
that the Port supports, including those that it does not intend to use.
 The next state is Configuration after eight consecutive TS2 Ordered Sets, with Link and Lane
15 numbers set to PAD, are received on any Lanes that detected a Receiver during Detect, and 16
TS2 Ordered Sets are transmitted after receiving one TS2 Ordered Set.
 Otherwise, next state is Detect after a 48 ms timeout.
PCI Express Base Specification, Rev. 4.0 Version 1.0
301
4.2.6.2.4 Polling.Speed
This state is unreachable given that the Link comes up to L0 in 2.5 GT/s data rate only and changes
speed by entering Recovery.
IMPLEMENTATION NOTE
5 Support for Higher Data Rates than 2.5 GT/s
A Link will initially train to the L0 state at the 2.5 GT/s data rate even if both sides are capable of
operating at a data rate greater than 2.5 GT/s. Supported higher data rates are advertised in the TS
Ordered Sets. The other side’s speed capability is registered during the Configuration.Complete
substate. Based on the highest supported common data rate, either side can initiate a change in
10 speed from the L0 state by transitioning to Recovery.
Figure 4-25: Polling Substate Machine
OM13801B
Polling.Active Polling.Compliance
Polling.Configuration
Entry
Polling
Exit to
Configuration
Exit to
Detect
PCI Express Base Specification, Rev. 4.0 Version 1.0
302
4.2.6.3 Configuration
The Configuration substate machine is shown in Figure 4-26.
4.2.6.3.1 Configuration.Linkwidth.Start
4.2.6.3.1.1 Downstream Lanes
5  Next state is Disabled if directed.
o Note: “if directed” applies to a Downstream Port that is instructed by a higher Layer to
assert the Disable Link bit (TS1 and TS2) on all Lanes that detected a Receiver during
Detect.
 Next state is Loopback if directed to this state, and the Transmitter is capable of being a
10 loopback master, which is determined by implementation specific means.
o Note: “if directed” applies to a Port that is instructed by a higher Layer to assert the
Loopback bit (TS1 and TS2) on all Lanes that detected a Receiver during Detect.
 In the optional case where a crosslink is supported, the next state is Disabled after all Lanes that
are transmitting TS1 Ordered Sets receive two consecutive TS1 Ordered Sets with the Disable
15 Link bit asserted.
 Next state is Loopback after all Lanes that are transmitting TS1 Ordered Sets, that are also
receiving Ordered Sets, receive the Loopback bit asserted in two consecutive TS1 Ordered Sets.
Note that the device receiving the Ordered Set with the Loopback bit set becomes the loopback
slave.
20  The Transmitter sends TS1 Ordered Sets with selected Link numbers and sets Lane numbers to
PAD on all the active Downstream Lanes if LinkUp is 0b or if the LTSSM is not initiating
upconfiguration of the Link width. In addition, if upconfigure_capable is set to 1b, and the
LTSSM is not initiating upconfiguration of the Link width, the LTSSM sends TS1 Ordered Sets
with the selected Link number and sets the Lane number to PAD on each inactive Lane after it
25 detected an exit from Electrical Idle since entering Recovery and has subsequently received two
consecutive TS1 Ordered Sets with the Link and Lane numbers each set to PAD while in this
substate.
o On transition to this substate from Polling, any Lane that detected a Receiver during
Detect is considered an active Lane.
30 o On transition to this substate from Recovery, any Lane that is part of the configured
Link the previous time through Configuration.Complete is considered an active Lane.
o The Data Rate Identifier Symbol of the TS1 Ordered Sets must advertise all data rates
that the Port supports, including those that it does not intend to use.
PCI Express Base Specification, Rev. 4.0 Version 1.0
303
If LinkUp is 1b and the LTSSM is initiating upconfiguration  of the Link width, initially it
transmits TS1 Ordered Sets with both the Link and Lane numbers set to PAD on the current set
of active Lanes; the inactive Lanes it intends to activate; and those Lanes where it detected an
exit from Electrical Idle since entering Recovery and has received two consecutive TS1 Ordered
5 Sets with the Link and Lane numbers each set to PAD. The LTSSM transmits TS1 Ordered
Sets with the selected Link number and the Lane number set to PAD when each of the Lanes
transmitting TS1 Ordered Sets receives two consecutive TS1 Ordered Sets with the Link and
Lane numbers each set to PAD or 1 ms has expired since entering this substate.
o After activating any inactive Lane, the Transmitter must wait for its TX common mode
10 to settle before exiting from Electrical Idle and transmitting the TS1 Ordered Sets.
o Link numbers are only permitted to be different for groups of Lanes capable of being a
unique Link.
o Note: An example of Link number assignments is a set of eight Downstream Lanes
capable of negotiating to become one x8 Port when connected to one component or
15 two x4 Ports when connected to two different components. The Downstream Lanes
send out TS1 Ordered Sets with the Link number set to N on four Lanes and Link
number set to N+1 on the other four Lanes. The Lane numbers are all set to PAD.
 If any Lanes first received at least one or more TS1 Ordered Sets with a Link and Lane number
set to PAD, the next state is Configuration.Linkwidth.Accept immediately after any of those
20 same Downstream Lanes receive two consecutive TS1 Ordered Sets with a non-PAD Link
number that matches any of the transmitted Link numbers, and with a Lane number set to PAD.
o If the crosslink configuration is not supported, the condition of first receiving a Link and
Lane number set to PAD is always true.
 Else: Optionally, if LinkUp is 0b and if crosslinks are supported, then all Downstream Lanes
25 that detected a Receiver during Detect must first transmit 16 to 32 TS1 Ordered Sets with a
non-PAD Link number and PAD Lane number and after this occurs if any Downstream Lanes
receive two consecutive TS1 Ordered Sets with a Link number different than PAD and a Lane
Number set to PAD, the Downstream Lanes are now designated as Upstream Lanes and a new
random crosslink timeout is chosen (see Tcrosslink in Table 8-3). The next state is
30 Configuration.Linkwidth.Start as Upstream Lanes.
o Note: This supports the optional crosslink where both sides may try to act as a
Downstream Port. This is resolved by making both Ports become Upstream and
assigning a random timeout until one side of the Link becomes a Downstream Port and
the other side remains an Upstream Port. This timeout must be random even when
35 hooking up two of the same devices so as to eventually break any possible deadlock.
o If crosslinks are supported, receiving a sequence of TS1 Ordered Sets with a Link
number of PAD followed by a Link number of non-PAD that matches the transmitted
Link number is only valid when not interrupted by the reception of a TS2 Ordered Set.
PCI Express Base Specification, Rev. 4.0 Version 1.0
304
IMPLEMENTATION NOTE
Crosslink Initialization
In the case where the Downstream Lanes are connected to both Downstream Lanes (crosslink) and
Upstream Lanes, the Port with the Downstream Lanes may continue with a single LTSSM as
described in this section or optionally, 5 split into multiple LTSSMs.
 The next state is Detect after a 24 ms timeout.
4.2.6.3.1.2 Upstream Lanes
 In the optional case where crosslinks are supported the next state is Disabled if directed.
o Note: “if directed” only applies to an optional crosslink Port that is instructed by a
10 higher Layer to assert the Disable Link bit (TS1 and TS2) on all Lanes that detected a
Receiver during Detect.
 Next state is Loopback if directed to this state, and the Transmitter is capable of being a
loopback master, which is determined by implementation specific means.
o Note: “if directed” applies to a Port that is instructed by a higher Layer to assert the
15 Loopback bit (TS1 and TS2) on all Lanes that detected a Receiver during Detect.
 Next state is Disabled after any Lanes that are transmitting TS1 Ordered Sets receive two
consecutive TS1 Ordered Sets with the Disable Link bit asserted.
o In the optional case where a crosslink is supported, the next state is Disabled only after
all Lanes that are transmitting TS1 Ordered Sets, that are also receiving TS1 Ordered
20 Sets, receive the Disable Link bit asserted in two consecutive TS1 Ordered Sets.
 Next state is Loopback after all Lanes that are transmitting TS1 Ordered Sets, that are also
receiving TS1 Ordered Sets, receive the Loopback bit asserted in two consecutive TS1 Ordered
Sets.
o Note: The device receiving the Ordered Set with the Loopback bit set becomes the
25 loopback slave.
 The Transmitter sends out TS1 Ordered Sets with Link numbers and Lane numbers set to PAD
on all the active Upstream Lanes; the inactive Lanes it is initiating to upconfigure the Link width;
and if upconfigure_capable is set to 1b, on each of the inactive Lanes where it detected an exit
from Electrical Idle since entering Recovery and has subsequently received two consecutive TS1
30 Ordered Sets with Link and Lane numbers, each set to PAD, in this substate.
o On transition to this substate from Polling, any Lane that detected a Receiver during
Detect is considered an active Lane.
o On transition to this substate from Recovery, any Lane that is part of the configured
Link the previous time through Configuration.Complete is considered an active Lane.
35 o On transition to this substate from Recovery, if the transition is not caused by LTSSM
timeout, the Transmitter must set the Autonomous Change (Symbol 4 bit 6) to 1b in the
TS1 Ordered Sets that it sends while in the Configuration state if the Transmitter intends
to change the Link width for autonomous reasons.
PCI Express Base Specification, Rev. 4.0 Version 1.0
305
o The Data Rate Identifier Symbol of the TS1 Ordered Sets must advertise all data rates
that the Port supports, including those that it does not intend to use.
If any Lane receives two consecutive TS1 Ordered Sets with Link numbers  that are different
than PAD and Lane number set to PAD, a single Link number is selected and Lane number set
5 to PAD are transmitted on all Lanes that both detected a Receiver and also received two
consecutive TS1 Ordered Sets with Link numbers that are different than PAD and Lane number
set to PAD. Any left over Lanes that detected a Receiver during Detect must transmit TS1
Ordered Sets with the Link and Lane number set to PAD. The next state is
Configuration.Linkwidth.Accept:
10 o If the LTSSM is initiating upconfiguration of the Link width, it waits until it receives two
consecutive TS1 Ordered Sets with a non-PAD Link Number and a PAD Lane number
on all the inactive Lanes it wants to activate, or, 1 ms after entry to this substate, it
receives two consecutive TS1 Ordered Sets on any Lane with a non-PAD Link number
and PAD Lane number, whichever occurs earlier, before transmitting TS1 Ordered Sets
15 with selected Link number and Lane number set to PAD.
o It is recommended that any possible multi-Lane Link that received an error in a TS1
Ordered Set or lost 128b/130b Block Alignment on a subset of the received Lanes; delay
the evaluation listed above by an additional two, or more, TS1 Ordered Sets when using
8b/10b encoding, or by an additional 34, or more, TS1 Ordered Sets when using
20 128b/130b encoding, but must not exceed 1 ms, so as not to prematurely configure a
smaller Link than possible.
 After activating any inactive Lane, the Transmitter must wait for its TX common
mode to settle before exiting Electrical Idle and transmitting the TS1 Ordered
Sets.
25  Optionally, if LinkUp is 0b and if crosslinks are supported, then all Upstream Lanes that
detected a Receiver during Detect must first transmit 16–32 TS1 Ordered Sets with a PAD Link
number and PAD Lane number and after this occurs and if any Upstream Lanes first receive
two consecutive TS1 Ordered Sets with Link and Lane numbers set to PAD, then:
o The Transmitter continues to send out TS1 Ordered Sets with Link numbers and Lane
30 numbers set to PAD.
o If any Lanes receive two consecutive TS1 Ordered Sets with Link numbers that are
different than PAD and Lane number set to PAD, a single Link number is selected and
Lane number set to PAD are transmitted on all Lanes that both detected a Receiver and
also received two consecutive TS1 Ordered Sets with Link numbers that are different
35 than PAD and Lane number set to PAD. Any left over Lanes that detected a Receiver
during Detect must transmit TS1 Ordered Sets with the Link and Lane number set to
PAD. The next state is Configuration.Linkwidth.Accept.
 It is recommended that any possible multi-Lane Link that received an error in a
TS1 Ordered Set or lost 128b/130b Block Alignment on a subset of the received
40 Lanes; delay the evaluation listed above by an additional two, or more, TS1
Ordered Sets when using 8b/10b encoding, or by an additional 34, or more, TS1
Ordered Sets when using 128b/130b encoding, but must not exceed 1 ms, so as
not to prematurely configure a smaller Link than possible.
PCI Express Base Specification, Rev. 4.0 Version 1.0
306
o Otherwise, after a Tcrosslink timeout, 16 to 32 TS2 Ordered Sets with PAD Link numbers
and PAD Lane numbers are sent. The Upstream Lanes become Downstream Lanes and
the next state is Configuration.Linkwidth.Start as Downstream Lanes.
 Note: This optional behavior is required for crosslink behavior where two Ports
may start off with Upstream Ports, and one will eventually 5 take the lead as a
Downstream Port.
 The next state is Detect after a 24 ms timeout.
4.2.6.3.2 Configuration.Linkwidth.Accept
4.2.6.3.2.1 Downstream Lanes
10  If a configured Link can be formed with at least one group of Lanes that received two
consecutive TS1 Ordered Sets with the same received Link number (non-PAD and matching
one that was transmitted by the Downstream Lanes), TS1 Ordered Sets are transmitted with the
same Link number and unique non-PAD Lane numbers are assigned to all these same Lanes.
The next state is Configuration.Lanenum.Wait.
15 o The assigned non-PAD Lane numbers must range from 0 to n-1, be assigned
sequentially to the same grouping of Lanes that are receiving the same Link number, and
Downstream Lanes which are not receiving TS1 Ordered Sets must not disrupt the
initial sequential numbering of the widest possible Link. Any left over Lanes must
transmit TS1 Ordered Sets with the Link and Lane number set to PAD.
20 o It is recommended that any possible multi-Lane Link that received an error in a TS1
Ordered Set or lost 128b/130b Block Alignment on a subset of the received Lanes delay
the evaluation listed above by an additional two, or more, TS1 Ordered Sets when using
8b/10b encoding, or by an additional 34, or more, TS1 Ordered Sets when using
128b/130b encoding, but must not exceed 1 ms, so as not to prematurely configure a
25 smaller Link than possible.
 The next state is Detect after a 2 ms timeout or if no Link can be configured or if all Lanes
receive two consecutive TS1 Ordered Sets with Link and Lane numbers set to PAD.
4.2.6.3.2.2 Upstream Lanes
 If a configured Link can be formed using Lanes that transmitted a non-PAD Link number
30 which are receiving two consecutive TS1 Ordered Sets with the same non-PAD Link number
and any non-PAD Lane number, TS1 Ordered Sets are transmitted with the same non-PAD
Link number and Lane numbers that, if possible, match the received Lane numbers or are
different, if necessary, (i.e., Lane reversed). The next state is Configuration.Lanenum.Wait.
o The newly assigned Lane numbers must range from 0 to m-1, be assigned sequentially
35 only to some continuous grouping of Lanes that are receiving non-PAD Lane numbers
(i.e., Lanes which are not receiving any TS1 Ordered Sets always disrupt a continuous
grouping and must not be included in this grouping), must include either Lane 0 or Lane
n-1 (largest received Lane number), and m-1 must be equal to or smaller than the largest
PCI Express Base Specification, Rev. 4.0 Version 1.0
307
received Lane number (n-1). Remaining Lanes must transmit TS1 Ordered Sets with
Link and Lane numbers set to PAD.
o It is recommended that any possible multi-Lane Link that received an error in a TS1
Ordered Set or lost 128b/130b Block Alignment on a subset of the received Lanes delay
the evaluation listed above by an additional two, or more, 5 TS1 Ordered Sets when using
8b/10b encoding, or by an additional 34, or more, TS1 Ordered Sets when using
128b/130b encoding, but must not exceed 1 ms, so as not to prematurely configure a
smaller Link than possible.
 The next state is Detect after a 2 ms timeout or if no Link can be configured or if all Lanes
10 receive two consecutive TS1 Ordered Sets with Link and Lane numbers set to PAD.
PCI Express Base Specification, Rev. 4.0 Version 1.0
308
IMPLEMENTATION NOTE
Example Cases
Notable examples related to the configuration of Downstream Lanes:
1. A x8 Downstream Port, which can be divided into two x4 Links, sends two different Link numbers on to
two x4 Upstream Ports. The Upstream Ports respond simultaneously by picking the two Link numbers.
The Downstream Port will have to choose one of these sets of Link numbers to configure as a Link, and
leave the other for a secondary LTSSM to configure (which will ultimately happen in
Configuration.Complete).
2. A x16 Downstream Port, which can be divided into two x8 Links, is hooked up to a x12 Upstream Port
that can be configured as a x12 Link or a x8 and a x4 Link. During Configuration.Linkwidth.Start the
Upstream Port returned the same Link number on all 12 Lanes. The Downstream Port would then
return the same received Link number and assign Lane numbers on the eight Lanes that can form a x8
Link with the remaining four Lanes transmitting a Lane number and a Link number set to PAD.
3. A x8 Downstream Port where only seven Lanes are receiving TS1 Ordered Sets with the same received
Link number (non-PAD and matching one that was transmitted by the Downstream Lanes) and an
eighth Lane, which is in the middle or adjacent to those same Lanes, is not receiving a TS1 Ordered Set.
In this case, the eighth Lane is treated the same as the other seven Lanes and Lane numbering for a x8
Lane should occur as described above.
Notable examples related to the configuration of Upstream Lanes:
A x8 Upstream Port is presented with Lane numbers that are backward from the preferred
numbering. If the optional behavior of Lane reversal is supported by the Upstream Port, the
Upstream Port transmits the same Lane numbers back to the Downstream Port. Otherwise the
opposite Lane numbers are transmitted back to the Downstream Port, and it will be up to the
Downstream Port to optionally fix the Lane ordering or exit Configuration.
Optional Lane reversal behavior is required to configure a Link where the Lane numbers are reversed
and the Downstream Port does not support Lane reversal. Specifically, the Upstream Port Lane
reversal will accommodate the scenario where the default Upstream sequential Lane numbering (0 to
n-1) is receiving a reversed Downstream sequential Lane number (n-1 to 0).
A x8 Upstream Port is not receiving TS1 Ordered Sets on the Upstream Port Lane 0:
a. In the case where the Upstream Port can only support a x8 or x1 Link and the Upstream Port can
support Lane reversal. The Upstream Port will assign a Lane 0 to only the received Lane 7 (received
Lane number n-1) and the remaining seven Lanes must transmit TS1 Ordered Sets with Link and
Lane numbers set to PAD.
b. In the case where the Upstream Port can only support a x8 or x1 Link and the Upstream Port cannot
support Lane reversal. No Link can be formed and the Upstream Port will eventually timeout after 2
ms and exit to Detect.
An optional x8 Upstream crosslink Port, which can be divided into two x4 Links, is attached to
two x4 Downstream Ports that present the same Link number, and each x4 Downstream Port
presents Lane numbers simultaneously that were each numbered 0 to 3. The Upstream Port will
have to choose one of these sets of Lane numbers to configure as a Link, and leave the other for
a second pass through Configuration.
PCI Express Base Specification, Rev. 4.0 Version 1.0
309
4.2.6.3.3 Configuration.Lanenum.Accept
4.2.6.3.3.1 Downstream Lanes
 If two consecutive TS1 Ordered Sets are received with non-PAD Link and non-PAD Lane
numbers that match all the non-PAD Link and non-PAD Lane numbers (or reversed Lane
5 numbers if Lane reversal is optionally supported) that are being transmitted in Downstream
Lane TS1 Ordered Sets, the next state is Configuration.Complete. Note that Retimers are
permitted to delay the transition to Configuration.Complete, as described in Section 4.3.8.
o The Link Bandwidth Management Status and Link Autonomous Bandwidth Status bits
of the Link Status register must be updated as follows on a Link bandwidth change if the
10 current transition to Configuration state was from the Recovery state:
(a) If the bandwidth change was initiated by the Downstream Port due to reliability issues,
the Link Bandwidth Management Status bit is Set.
(b) Else if the bandwidth change was not initiated by the Downstream Port and the
Autonomous Change bit (Symbol 4 bit 6) in two consecutive received TS1 Ordered
15 Sets is 0b, the Link Bandwidth Management Status bit is Set.
(c) Else the Link Autonomous Bandwidth Status bit is Set.
o The condition of Reversed Lane numbers is defined strictly as the Downstream Lane 0
receiving a TS1 Ordered Set with a Lane number equal to n-1 and the Downstream Lane
n-1 receiving a TS1 Ordered Set with a Lane number equal to 0.
20 o It is recommended that any possible multi-Lane Link that received an error in a TS1
Ordered Set or lost 128b/130b Block Alignment on a subset of the received Lanes delay
the evaluation listed above by an additional two, or more, TS1 Ordered Sets when using
8b/10b encoding, or by an additional 34, or more, TS1 Ordered Sets when using
128b/130b encoding, but must not exceed 1 ms, so as not to prematurely configure a
25 smaller Link than possible.
 If a configured Link can be formed with any subset of the Lanes that receive two consecutive
TS1 Ordered Sets with the same transmitted non-PAD Link numbers and any non-PAD Lane
numbers, TS1 Ordered Sets are transmitted with the same non-PAD Link numbers and new
Lane numbers assigned and the next state is Configuration.Lanenum.Wait.
30 o The newly assigned transmitted Lane numbers must range from 0 to m-1, be assigned
sequentially only to some continuous grouping of the Lanes that are receiving non-PAD
Lane numbers (i.e., Lanes which are not receiving any TS1 Ordered Sets always disrupt a
continuous grouping and must not be included in this grouping), must include either
Lane 0 or Lane n-1 (largest received Lane number), and m-1 must be equal to or smaller
35 than the largest received Lane number (n-1). Any left over Lanes must transmit TS1
Ordered Sets with the Link and Lane number set to PAD.
o It is recommended that any possible multi-Lane Link that received an error in a TS1
Ordered Set or lost 128b/130b Block Alignment on a subset of the received Lanes delay
the evaluation listed above by an additional two, or more, TS1 Ordered Sets when using
40 8b/10b encoding, or by an additional 34, or more, TS1 Ordered Sets when using
PCI Express Base Specification, Rev. 4.0 Version 1.0
310
128b/130b encoding, but must not exceed 1 ms, so as not to prematurely configure a
smaller Link than possible.
The next state is Detect if no Link can be configured or if all Lanes receive  two consecutive TS1
Ordered Sets with Link and Lane numbers set to PAD.
5 4.2.6.3.3.2 Upstream Lanes
 If two consecutive TS2 Ordered Sets are received with non-PAD Link and non-PAD Lane
numbers that match all non-PAD Link and non-PAD Lane numbers that are being transmitted
in Upstream Lane TS1 Ordered Sets, the next state is Configuration.Complete. Note that
Retimers are permitted to delay the transition to Configuration.Complete, as described in
10 Section 4.3.8.
 If a configured Link can be formed with any subset of the Lanes that receive two consecutive
TS1 Ordered Sets with the same transmitted non-PAD Link numbers and any non-PAD Lane
numbers, TS1 Ordered Sets are transmitted with the same non-PAD Link numbers and new
Lane numbers assigned and the next state is Configuration.Lanenum.Wait.
15 o The newly assigned transmitted Lane numbers must range from 0 to m-1, be assigned
sequentially only to some continuous grouping of Lanes that are receiving non-PAD
Lane numbers (i.e., Lanes which are not receiving any TS1 Ordered Sets always disrupt a
continuous grouping and must not be included in this grouping), must include either
Lane 0 or Lane n-1 (largest received Lane number), and m-1 must be equal to or smaller
20 than the largest received Lane number (n-1). Any left over Lanes must transmit TS1
Ordered Sets with the Link and Lane number set to PAD.
o It is recommended that any possible multi-Lane Link that received an error in a TS1
Ordered Set or lost 128b/130b Block Alignment on a subset of the received Lanes delay
the evaluation listed above by an additional two, or more, TS1 Ordered Sets when using
25 8b/10b encoding, or by an additional 34, or more, TS1 Ordered Sets when using
128b/130b encoding, but must not exceed 1 ms, so as not to pre-maturely configure a
smaller Link than possible.
 The next state is Detect if no Link can be configured or if all Lanes receive two consecutive TS1
Ordered Sets with Link and Lane numbers set to PAD.
PCI Express Base Specification, Rev. 4.0 Version 1.0
311
4.2.6.3.4 Configuration.Lanenum.Wait
4.2.6.3.4.1 Downstream Lanes
 The next state is Configuration.Lanenum.Accept if any of the Lanes that detected a Receiver
during Detect receive two consecutive TS1 Ordered Sets which have a Lane number different
5 from when the Lane first entered Configuration.Lanenum.Wait, and not all the Lanes’ Link
numbers are set to PAD or two consecutive TS1 Ordered Sets have been received on all Lanes,
with Link and Lane numbers that match what is being transmitted on all Lanes.
The Upstream Lanes are permitted delay up to 1 ms before transitioning to
Configuration.Lanenum.Accept.
10 The reason for delaying up to 1 ms before transitioning is to prevent received errors or skew
between Lanes affecting the final configured Link width.
The condition of requiring reception of any Lane number different from when the Lane(s) first
entered Configuration.Lanenum.Wait is necessary in order to allow the two Ports to settle on an
agreed upon Link width. The exact meaning of the statement “any of the Lanes receive two
15 consecutive TS1 Ordered Sets, which have a Lane number different from when the Lane first
entered Configuration.Lanenum.Wait” requires that a Lane number must have changed from
when the Lanes most recently entered Configuration.Lanenum.Wait before a transition to
Configuration.Lanenum.Accept can occur.
 The next state is Detect after a 2 ms timeout or if all Lanes receive two consecutive TS1
20 Ordered Sets with Link and Lane numbers set to PAD.
4.2.6.3.4.2 Upstream Lanes
 The next state is Configuration.Lanenum.Accept
(a) If any of the Lanes receive two consecutive TS1 Ordered Sets that have a Lane number
different from when the Lane first entered Configuration.Lanenum.Wait, and not all the
25 Lanes’ Link numbers are set to PAD
or
(b) If any Lane receives two consecutive TS2 Ordered Sets
 The next state is Detect after a 2 ms timeout or if all Lanes receive two consecutive TS1
Ordered Sets with Link and Lane numbers set to PAD.
30 4.2.6.3.5 Configuration.Complete
A device is allowed to change the supported data rates and upconfigure capability that it advertises
when it enters this substate, but it must not change those values while in this substate.
4.2.6.3.5.1 Downstream Lanes
 TS2 Ordered Sets are transmitted using Link and Lane numbers that match the received TS1
35 Ordered Set Link and Lane numbers.
PCI Express Base Specification, Rev. 4.0 Version 1.0
312
o The Upconfigure Capability bit of the TS2 Ordered Sets is permitted to be set to 1b to
indicate that the Port is capable of supporting a x1 Link on the currently assigned Lane 0
and up-configuring the Link while LinkUp = 1b. Advertising this capability is optional.
N_FTS must be noted for  use in L0s when leaving this state.
5  When using 8b/10b encoding, Lane-to-Lane de-skew must be completed when leaving this
state.
 Scrambling is disabled if all configured Lanes have the Disable Scrambling bit asserted in two
consecutively received TS2 Ordered Sets.
o The Port that is sending the Disable Scrambling bit on all of the configured Lanes must
10 also disable scrambling. Scrambling can only be disabled when using 8b/10b encoding.
 The next state is Configuration.Idle immediately after all Lanes that are transmitting TS2
Ordered Sets receive eight consecutive TS2 Ordered Sets with matching Lane and Link numbers
(non-PAD) and identical data rate identifiers (including identical Link Upconfigure Capability
(Symbol 4 bit 6)), and 16 TS2 Ordered Sets are sent after receiving one TS2 Ordered Set.
15 Implementations with the Retimer Presence Detect Supported bit of the Link Capabilities 2
register set to 1b must also receive the eight consecutive TS2 Ordered Sets with identical
Retimer Present (Symbol 5 bit 4) when the data rate is 2.5 GT/s. Implementations with Two
Retimers Presence Detect Supported bit of the Link Capabilities 2 register set to 1b must also
receive the eight consecutive TS2 Ordered Sets with identical Retimer Present (Symbol 5 bits
20 5:4) when the data rate is 2.5 GT/s.
o If the data rate of operation is 2.5 GT/s:
 If the Retimer Presence Detect Supported bit of the Link Capabilities 2 register
is set to 1b and any Configured Lane received the Retimer Present bit set to 1b
in the eight consecutively received TS2 Ordered Sets, then the Retimer Presence
25 Detected bit must be set to 1b in the Link Status 2 Register otherwise the
Retimer Presence Detected bit must be set to 0b in the Link Status 2 Register.
 If the Two Retimers Presence Detect Supported bit of the Link Capabilities 2
register is set to 1b and any configured Lane received the Two Retimers Present
bit set to 1b in the eight consecutively received TS2 Ordered Sets then the Two
30 Retimers Presence Detected bit must be set to 1b in the Link Status 2 Register,
otherwise the Two Retimers Presence Detected bit must be set to 0b.
o If the device supports greater than 2.5 GT/s data rate, it must record the data rate
identifier received on any configured Lane of the Link. This will override any previously
recorded value. A variable to track speed change in recovery state,
35 changed_speed_recovery, is reset to 0b.
o If the device sends TS2 Ordered Sets with the Link Upconfigure Capability (Symbol 4
bit 6) set to 1b, and receives eight consecutive TS2 Ordered Sets with the Link
Upconfigure Capability bit set to 1b, the variable upconfigure_capable is set to 1b, else it
is reset to 0b.
PCI Express Base Specification, Rev. 4.0 Version 1.0
313
o All remaining Lanes that are not part of the configured Link are no longer associated
with the LTSSM in progress and must:
i. Be associated with a new LTSSM if this optional feature is supported.
or
ii. All Lanes that cannot be associated with an optional 5 new LTSSM must transition to
Electrical Idle.56 Those Lanes that formed a Link up to the L0 state, and LinkUp has
been 1b since then, but are not a part of the currently configured Link, must be
associated with the same LTSSM if the LTSSM advertises Link width upconfigure
capability. It is recommended that the Receiver terminations of these Lanes be left on.
10 If they are not left on, they must be turned on when the LTSSM enters the
Recovery.RcvrCfg substate until it reaches the Configuration.Complete substate if
upconfigure_capable is set to 1b to allow for potential Link width upconfiguration. Any
Lane that was not part of the LTSSM during the initial Link training through L0 cannot
become a part of the LTSSM as part of the Link width upconfiguration process.
15  In the case of an optional crosslink, the Receiver terminations are required to
meet ZRX-HIGH-IMP-DC-POS and ZRX-HIGH-IMP-DC-NEG (see Table 8-11).
 These Lanes must be re-associated with the LTSSM immediately after the
LTSSM in progress transitions back to Detect.
 An EIOS does not need to be sent before transitioning to Electrical Idle, and the
20 transition to Electrical Idle does not need to occur on a Symbol or Ordered Set
boundary.
 After a 2 ms timeout:
 The next state is Detect if the current data rate is 2.5 GT/s or 5.0 GT/s.
 The next state is Configuration.Idle if the idle_to_rlock_transitioned variable is
25 less than FFh and the current data rate is 8.0 GT/s or higher.
i. The changed_speed_recovery variable is reset to 0b.
ii. Lanes that are not part of the configured Link are no longer associated with the
LTSSM in progress and must meet requirement (i) or (ii) specified above for the nontimeout
transition to Configuration.Idle.
30 iii. The upconfigure_capable variable is permitted, but not required, to be updated if at
least one Lane received eight consecutive TS2 Ordered Sets with matching Lane and
Link numbers (non-PAD). If updated, the upconfigure_capable variable is set to 1b
when the transmitted and received Link Upconfigure Capability bits are 1b, else it is reset
to 0b.
35 o Else the next state is Detect.
56 The common mode being driven does not need to meet the Absolute Delta Between DC Common Mode During L0
and Electrical Idle (VTX-CM-DC-ACTIVE-IDLE-DELTA) specification (see Table 8-7).
PCI Express Base Specification, Rev. 4.0 Version 1.0
314
4.2.6.3.5.2 Upstream Lanes
TS2 Ordered Sets are transmitted using Link and Lane numbers that  match the received TS2
Link and Lane numbers.
o The Upconfigure Capability bit of the TS2 Ordered Sets is permitted to be set to 1b to
5 indicate that the Port is capable of supporting a x1 Link on the currently assigned Lane 0
and up-configuring the Link while LinkUp = 1b. Advertising this capability is optional.
 N_FTS must be noted for use in L0s when leaving this state.
 When using 8b/10b encoding, Lane-to-Lane de-skew must be completed when leaving this
state.
10  Scrambling is disabled if all configured Lanes have the Disable Scrambling bit asserted in two
consecutively received TS2 Ordered Sets.
o The Port that is sending the Disable Scrambling bit on all of the configured Lanes must
also disable scrambling. Scrambling can only be disabled when using 8b/10b encoding.
 The next state is Configuration.Idle immediately after all Lanes that are transmitting TS2
15 Ordered Sets receive eight consecutive TS2 Ordered Sets with matching Lane and Link numbers
(non-PAD) and identical data rate identifiers (including identical Link Upconfigure Capability
(Symbol 4 bit 6)), and 16 consecutive TS2 Ordered Sets are sent after receiving one TS2
Ordered Set. Implementations with the Retimer Presence Detect Supported bit of the Link
Capabilities 2 register set to 1b must also receive the eight consecutive TS2 Ordered Sets with
20 identical Retimer Present (Symbol 5 bit 4) when the data rate is 2.5 GT/s. Implementations with
Two Retimers Presence Detect Supported bit of the Link Capabilities 2 register set to 1b must
also receive the eight consecutive TS2 Ordered Sets with identical Retimer Present
(Symbol 5 bits 5:4) when the data rate is 2.5 GT/s.
o If the data rate of operation is 2.5 GT/s:
25  If the Retimer Presence Detect Supported bit of the Link Capabilities 2 register
is set to 1b and any Configured Lane received the Retimer Present bit set to 1b
in the eight consecutively received TS2 Ordered Sets, then the Retimer Presence
Detected bit must be set to 1b in the Link Status 2 Register otherwise the
Retimer Presence Detected bit must be set to 0b in the Link Status 2 Register.
30  If the Two Retimers Presence Detect Supported bit of the Link Capabilities 2
register is set to 1b and any configured Lane received the Two Retimers Present
bit set to 1b in the eight consecutively received TS2 Ordered Sets then the Two
35 Retimers Presence Detected bit must be set to 1b in the Link Status 2
Register, otherwise the Two Retimers Presence Detected bit must be set to 0b.
35 o If the device supports greater than 2.5 GT/s data rate, it must record the data rate
identifier received on any configured Lane of the Link. This will override any previously
recorded value. A variable to track speed change in recovery state,
changed_speed_recovery, is reset to 0b.
o If the device sends TS2 Ordered Sets with the Link Upconfigure Capability (Symbol 4
40 bit 6) set to 1b, as well as receives eight consecutive TS2 Ordered Sets with the Link
PCI Express Base Specification, Rev. 4.0 Version 1.0
315
Upconfigure Capability bit set to 1b, the variable upconfigure_capable is set to 1b, else
it is reset to 0b.
o All remaining Lanes that are not part of the configured Link are no longer associated
with the LTSSM in progress and must:
i. Optionally be associated with a new crosslink LTSSM 5 if this feature is supported.
or
ii. All remaining Lanes that are not associated with a new crosslink LTSSM must
transition to Electrical Idle,57 and Receiver terminations are required to meet ZRX-HIGHIMP-
DC-POS and ZRX-HIGH-IMP-DC-NEG (see Table 8-11). Those Lanes that formed a Link up to
10 the L0 state, and LinkUp has been 1b since then, but are not a part of the currently
configured Link, must be associated with the same LTSSM if the LTSSM advertises Link
width upconfigure capability. It is recommended that the Receiver terminations of these
Lanes be left on. If they are not left on, they must be turned on when the LTSSM enters
the Recovery.RcvrCfg substate until it reaches the Configuration.Complete substate if
15 upconfigure_capable is set to 1b to allow for potential Link width upconfiguration. Any
Lane that was not part of the LTSSM during the initial Link training through L0 cannot
become a part of the LTSSM as part of the Link width upconfiguration process.
 These Lanes must be re-associated with the LTSSM immediately after the
LTSSM in progress transitions back to Detect.
20  EIOS does not need to be sent before transitioning to Electrical Idle, and the
transition to Electrical Idle does not need to occur on a Symbol or Ordered Set
boundary.
 After a 2 ms timeout:
o The next state is Detect if the current data rate is 2.5 GT/s or 5.0 GT/s.
25 The next state is Configuration.Idle if the idle_to_rlock_transitioned variable is less than FFh and
the current data rate is 8.0 GT/s or higher.
i. The changed_speed_recovery variable is reset to 0b.
ii. Lanes that are not part of the configured Link are no longer associated with the LTSSM
in progress and must meet requirement (i) or (ii) specified above for the non-timeout
30 transition to Configuration.Idle.
iii. The upconfigure_capable variable is permitted, but not required, to be updated if at least
one Lane received eight consecutive TS2 Ordered Sets with matching Lane and Link
numbers (non-PAD). If updated, the upconfigure_capable variable is set to 1b when the
transmitted and received Link Upconfigure Capability bits are 1b, else it is reset to 0b.
35 Else the next state is Detect.
57 The common mode being driven does not need to meet the Absolute Delta Between DC Common Mode During L0
and Electrical Idle (VTX-CM-DC-ACTIVE-IDLE-DELTA) specification (see Table 8-7).
PCI Express Base Specification, Rev. 4.0 Version 1.0
316
4.2.6.3.6 Configuration.Idle
 When using 8b/10b encoding, the Transmitter sends Idle data Symbols on all configured Lanes.
 When using 128b/130b encoding:
o If the data rate is 8.0 GT/s, the Transmitter sends one SDS Ordered Set on all
5 configured Lanes to start a Data Stream and then sends Idle data Symbols on all
configured Lanes. The first Idle data Symbol transmitted on Lane 0 is the first Symbol of
the Data Stream.
o If the data rate is 16.0 GT/s, the Transmitter sends one Control SKP Ordered Set
followed immediately by one SDS Ordered Set on all configured Lanes to start a Data
10 Stream and then sends Idle data Symbols on all configured Lanes. The first Idle data
Symbol transmitted on Lane 0 is the first Symbol of the Data Stream.
 Receiver waits for Idle data.
 LinkUp = 1b
 When using 8b/10b encoding, the next state is L0 if eight consecutive Symbol Times of Idle
15 data are received on all configured Lanes and 16 Idle data Symbols are sent after receiving one
Idle data Symbol.
o If software has written a 1b to the Retrain Link bit in the Link Control register since the
last transition to L0 from Recovery or Configuration, the Downstream Port must set the
Link Bandwidth Management Status bit of the Link Status register to 1b.
20  When using 128b/130b encoding, next state is L0 if eight consecutive Symbol Times of Idle
data are received on all configured Lanes, 16 Idle data Symbols are sent after receiving one Idle
data Symbol, and this state was not entered by a timeout from Configuration.Complete.
o The Idle data Symbols must be received in Data Blocks.
o Lane-to-Lane de-skew must be completed before Data Stream processing starts.
25 o If software has written a 1b to the Retrain Link bit in the Link Control register since the
last transition to L0 from Recovery or Configuration, the Downstream Port must set the
Link Bandwidth Management Status bit of the Link Status register to 1b.
o The idle_to_rlock_transitioned variable is reset to 00h on transition to L0.
PCI Express Base Specification, Rev. 4.0 Version 1.0
317
Otherwise,  after a minimum 2 ms timeout:
o If the idle_to_rlock_transitioned variable is less than FFh, the next state is
Recovery.RcvrLock.
♦ On transition to Recovery.RcvrLock:
5 ■ If the data rate is 8.0 GT/s or higher, the idle_to_rlock_transitioned variable is
incremented by 1.
■ If the data rate is 2.5 GT/s or 5.0 GT/s, the idle_to_rlock_transitioned variable is
set to FFh.
o Else the next state is Detect.
10
Figure 4-26: Configuration Substate Machine
Exit to
Recovery
OM13802C
Configuration.Linkwidth.Start
Configuration.Linkwidth.Accept
Configuration.Lanenum.Wait
Configuration.Lanenum.Accept
Configuration.Complete
Configuration.Idle
Entry
Configuration
Exit to
L0
Exit to
Loopback
Exit to
Disabled
Exit to
Detect
PCI Express Base Specification, Rev. 4.0 Version 1.0
318
4.2.6.4 Recovery
The Recovery substate machine is shown in Figure 4-27
4.2.6.4.1 Recovery.RcvrLock
If the Link is operating at a data rate of 8.0 GT/s or higher, a Receiver must consider any TS1 or
5 TS2 Ordered Set to be received only after it obtains Block Alignment in that Lane. If entry to this
substate is from L1 or Recovery.Speed or L0s, the Block Alignment must be obtained after exiting
Electrical Idle condition. If entry to this substate is from L0, the Block Alignment must be obtained
after the end of the last Data Stream.
 If the data rate of operation is 8.0 GT/s or higher:
10 o If the start_equalization_w_preset variable is set to 1b:
 An Upstream Port operating at 8.0 GT/s must use the 8.0 GT/s Transmitter
preset values it registered from the received eight consecutive EQ TS2 Ordered
Sets in Recovery.RcvrCfg in its Transmitter setting as soon as it starts
transmitting in 8.0 GT/s data rate and ensure that it meets the preset definition
15 in Chapter 8. Lanes that received a Reserved or unsupported Transmitter preset
value must use an implementation specific method to choose a supported
Transmitter preset setting for use as soon it starts transmitting at 8.0 GT/s. The
Upstream Port may optionally use the Receiver preset hint value suggested by
the Downstream Port in those EQ TS2 Ordered Sets.
20  An Upstream Port operating at 16.0 GT/s must use the 16.0 GT/s Transmitter
preset values it registered from the received eight consecutive 8GT EQ TS2
Ordered Sets in Recovery.RcvrCfg in its Transmitter setting as soon as it starts
transmitting in 16.0 GT/s data rate and ensure that it meets the preset definition
in Section 4.3. Lanes that received a Reserved or unsupported Transmitter preset
25 value must use an implementation specific method to choose a supported
Transmitter preset setting for use as soon as it starts transmitting at 16.0 GT/s.
 A Downstream Port operating at 8.0 GT/s must use the Downstream Port
8.0 GT/s Transmitter Preset field defined in the Lane Equalization Control
Register entry for each Lane as soon as it starts transmitting in 8.0 GT/s data
30 rate and ensure that it meets the preset definition in Chapter 8. Lanes that have a
Reserved or unsupported Transmitter Preset value in the Downstream Port
8.0 GT/s Transmitter Preset field of their associated 8.0 GT/s Lane
Equalization Control Register entry must use an implementation specific method
to choose a supported Transmitter preset setting for use as soon as it starts
35 transmitting at 8.0 GT/s. The Downstream Port may optionally use the
Downstream Port 8.0 GT/s Receiver Preset Hint field defined in the Lane
Equalization Control Register entry for each of its Receivers corresponding to
the Lane, if they are not Reserved values.
 A Downstream Port operating at 16.0 GT/s must use 16.0 GT/s Transmitter
40 preset settings as soon as it starts transmitting at the 16.0 GT/s data rate. The
PCI Express Base Specification, Rev. 4.0 Version 1.0
319
16.0 GT/s Transmitter preset settings must be chosen, for each configured Lane,
as follows:
1. If eight consecutive 8GT EQ TS2 Ordered Sets were received with supported
16.0 GT/s Transmitter Preset values in the most recent transition through
Recovery.RcvrCfg, the Transmitter Preset 5 value from those 8GT EQ TS2
Ordered Sets must be used.
2. Else, if the Transmitter Preset value defined in the 16.0 GT/s Downstream
Port Transmitter Preset field of the 16.0 GT/s Lane Equalization Control
Register entry is supported: the Transmitter Preset value from the 16.0 GT/s
10 Lane Equalization Control Register entry must be used.
3. Else, use an implementation specific method to choose a supported
Transmitter preset setting.
The Downstream Port must ensure that it meets the preset definition in Section
4.3.
15  Next state is Recovery.Equalization.
o Else:
 The Transmitter must use the coefficient settings agreed upon at the conclusion
of the last equalization procedure
 If this substate was entered from Recovery.Equalization, in the transmitted TS1
20 Ordered Sets, a Downstream Port must set the Pre-cursor, Cursor, and Postcursor
Coefficient fields to the current Transmitter settings, and if the last
accepted request in Phase 2 of Recovery.Equalization was a preset request, it
must set the Transmitter Preset field to the accepted preset of that request.
 It is recommended that in this substate, in the transmitted TS1 Ordered Sets, all
25 Ports set the Pre-cursor, Cursor, and Post-cursor Coefficient fields to the current
Transmitter settings, and set the Transmitter Preset field to the most recent
preset that the Transmitter settings were set to.
 An Upstream Port that receives eight consecutive TS1 Ordered Sets on all
configured Lanes with the following characteristics must transition to
30 Recovery.Equalization
• Link and Lane numbers in the received TS1 Ordered Sets match with the
Link and Lane numbers in the transmitted TS1 Ordered Sets on each
Lane
• speed_change bit is equal to 0b
35 • EC bits not equal to 00b
PCI Express Base Specification, Rev. 4.0 Version 1.0
320
IMPLEMENTATION NOTE
Redoing Equalization
A Downstream Port may use this provision to redo some parts of the Transmitter Equalization
process using software help or some other implementation specific means while ensuring no
transactions are in flight on the Link 5 to avoid any timeouts.
 Next state for a Downstream Port is Recovery.Equalization if directed and
Recovery.RcvrLock was not entered from Configuration.Idle or Recovery.Idle.
The Port must ensure that no more than 2 TS1 Ordered Sets with EC=00b are
transmitted due to being in Recovery.RcvrLock before starting to transmit the
10 TS1 Ordered Sets required by Recovery.Equalization.
 Transmitter sends TS1 Ordered Sets on all configured Lanes using the same Link and Lane
numbers that were set after leaving Configuration. The speed_change bit (bit 7 of the Data Rate
Identifier Symbol in TS1 Ordered Set) must be set to 1b if the directed_speed_change variable is
set to 1b. The directed_speed_change variable is set to 1b if any configured Lane receives eight
15 consecutive TS1 Ordered Sets with the speed_change bit set to 1b. Only those data rates greater
than 2.5 GT/s should be advertised that can be supported reliably. The N_FTS value in the
TS1 Ordered Set transmitted reflects the number at the current speed of operation. A device is
allowed to change the supported data rates that it advertises when it enters this substate. A
Downstream Port that intends to redo equalization with a data rate change from 2.5 GT/s or 5.0
20 GT/s to 8.0 GT/s must:
o Send EQ TS1 Ordered Sets with the speed_change bit set to 1b and advertising the 8.0
GT/s Data Rate Identifier.
o If the equalization redo attempt is initiated by the hardware as described in Section 4.2.3,
then hardware must ensure that the Data Rate is 2.5 GT/s or 5.0 GT/s before initiating
25 the attempt.
o If the equalization redo attempt is initiated by the software mechanism as described in
Section 4.2.3, then software must ensure that the Data Rate is 2.5 GT/s or 5.0 GT/s
before initiating the attempt.
An Upstream Port must advertise 8.0 GT/s data rate support in the TS2 Ordered Sets it transmits in
30 Recovery.RcvrCfg, and optionally in the TS1 Ordered Sets it transmits in this substate, if:
o The eight consecutive Ordered Sets it receives are EQ TS1 or EQ TS2 Ordered Sets
with the speed_change bit set to 1b and 8.0 GT/s data rate support is advertised by the
Downstream Port, unless the Upstream Port has determined that a problem unrelated to
equalization prevents it from operating reliably at 8.0 GT/s.
35 A Downstream Port that intends to redo equalization with a data rate change from 8.0 GT/s to 16.0
GT/s must:
o Send TS1 Ordered Sets with the Equalization Redo bit set to 1b, the speed_change bit
set to 1b, and advertising the 16.0 GT/s Data Rate Identifier.
o If the equalization redo attempt is initiated by the hardware as described in Section 4.2.3,
40 then hardware must ensure that the Data Rate is 8.0 GT/s before initiating the attempt.
PCI Express Base Specification, Rev. 4.0 Version 1.0
321
o If the equalization redo attempt is initiated by the software mechanism as described in
Section 4.2.3, then software must ensure that the Data Rate is 8.0 GT/s before initiating
the attempt.
An Upstream Port must advertise 16.0 GT/s data rate support in the TS2 Ordered Sets it transmits
in Recovery.RcvrCfg, and optionally in the TS1 Ordered Sets it transmits 5 in this substate, if:
o The eight consecutive Ordered Sets it receives are TS1 Ordered Sets with the
Equalization Redo bit set to 1b or 8GT EQ TS2 Ordered Sets with the speed_change bit
set to 1b, unless the Upstream Port has determined that a problem unrelated to 16.0
GT/s equalization prevents it from operating reliably at 16.0 GT/s.
10 Under other conditions, a device must not change the supported data rate values either in this
substate or while in the Recovery.RcvrCfg or Recovery.Equalization substates. The
successful_speed_negotiation variable is reset to 0b upon entry to this substate.
PCI Express Base Specification, Rev. 4.0 Version 1.0
322
IMPLEMENTATION NOTE
Handling a Request to Advertise 8.0 GT/s Data Rate Identifier
If an Upstream Port that is not advertising 8.0 GT/s Data Rate Identifiers receives EQ TSs with
8.0 GT/s Data Rate Identifiers and with the speed_change bit set in Recovery.RcvrLock, that
indicates that the Downstream Port is attempting to switch the Link 5 Speed to 8.0 GT/s in order to
perform the 8.0 GT/s Link Equalization Procedure. If for some reason the Upstream Port is unable
or unwilling to switch to advertising 8.0 GT/s Data Rate Identifiers in the TS2 Ordered Sets it
transmits once it transitions to Recovery.RcvrCfg, the 8.0 GT/s Link Equalization Procedure will
not be performed in the current tenure in Recovery. This may cause the Downstream Port to
10 permanently abandon its attempt to change the link speed to 8.0 GT/s and perform the 8.0 GT/s
Link Equalization Procedure, resulting in an operational link speed of less than 8.0 GT/s until after
the link transitions through Detect and is re-trained. It is recommended that if an Upstream Port is
for some temporary reason unable or unwilling to switch to advertising 8.0 GT/s Data Rate
Identifiers in the condition described above, and does not intend to prohibit the Link from
15 operating at 8.0 GT/s, that it perform one of the following two actions below as soon as is
reasonable for it to do so:
 If the Upstream Port supports the Quiesce Guarantee mechanism for performing the Link
Equalization Procedure, enter Recovery and advertise 8.0 GT/s Data Rate Identifiers with the
speed_change bit set to 1b in the TSs that it sends. If Recovery.Equalization is not entered
20 after changing speed to 8.0 GT/s and before entering Recovery.RcvrCfg at 8.0 GT/s (the
Downstream Port did not direct an entry to Recovery.Equalization), it should set the Request
Equalization and Quiesce Guarantee bits to 1b in the TS2 Ordered Sets sent at 8.0 GT/s in
Recovery.RcvrCfg in order to request the Downstream Port to initiate the Link Equalization
Procedure.
25  Enter Recovery and advertise 8.0 GT/s Data Rate Identifiers with the speed_change bit cleared
to 0b. The Downstream Port may then later initiate a speed change to 8.0 GT/s and perform
the Link Equalization Procedure, though there is no guarantee that it will do so.
The process for handling a request to advertise 16.0 GT/s Data Rate Identifier is similar to
8.0 GT/s Data Rate Identifier with 16.0 GT/s Data Rate Identifier substituting 8.0 GT/s Data Rate
30 Idenitifier and 8GT EQ TS2s substituting EQ TSs.
An Upstream Port must set the Selectable De-emphasis bit (bit 6 of Symbol 4) of the TS1
Ordered Sets it transmits to match the desired de-emphasis level at 5.0 GT/s. The mechanism
an Upstream Port may adopt to request a de-emphasis level if it chooses to do so is
implementation specific. It must also be noted that since the Upstream Port’s request may not
35 reach the Downstream Port due to bit errors in the TS1 Ordered Sets, the Upstream Port may
attempt to re-request the desired de-emphasis level in subsequent entries to Recovery state when
speed change is requested. If the Downstream Port intends to use the Upstream Port’s deemphasis
information in Recovery.RcvrCfg, then it must record the value of the Selectable Deemphasis
bit received in this state.
40 The Transmit Margin field of the Link Control 2 register is sampled on entry to this substate and
becomes effective on the transmit package pins within 192 ns of entry to this substate and
PCI Express Base Specification, Rev. 4.0 Version 1.0
323
remains effective until a new value is sampled on a subsequent entry to this substate from L0,
L0s, or L1.
o After activating any inactive Lane, the Transmitter must wait for its TX common mode
to settle before exiting Electrical Idle and transmitting the TS1 Ordered Sets with the
5 following exceptions.
o When exiting from the L1.2 L1 PM Substate, common mode is permitted to be
established passively during L1.0, and actively during Recovery. In order to ensure
common mode has been established in Recovery.RcvrLock, the Downstream Port must
maintain a timer, and the Downstream Port must not send TS2 training sequences until a
10 minimum of TCOMMONMODE has elapsed since the Downstream Port has started both
transmitting and receiving TS1 training sequences. See Section 5.5.3.3.
o Implementations must note that the voltage levels may change after an early bit lock and
Symbol or Block alignment since the new Transmit Margin field becomes effective
within 192 ns after the other side enter Recovery.RcvrLock. The Receiver needs to
15 reacquire bit lock and Symbol or Block alignment under those conditions.
a. Note: The directed_speed_change variable is set to 1b in L0 or L1 state for the side
that is initiating a speed change. For the side that is not initiating a speed change,
this bit is Set in this substate if the received TS Ordered Sets have the speed change
bit Set. This bit is reset to 0b in the Recovery.Speed substate.
20 b. A device must accept all good TLPs and DLLPs it receives after entering this
substate from L0 prior to receiving the first TS Ordered Set. If operating with
128b/130b encoding, any received TLPs and DLLPs are subject to the framing rules
for 128b/130b encoding in Section 4.2.2.3.
 Next state is Recovery.RcvrCfg if eight consecutive TS1 or TS2 Ordered Sets are received on all
25 configured Lanes with the same Link and Lane numbers that match what is being transmitted on
those same Lanes and the speed_change bit is equal to the directed_speed_change variable and
the EC field is 00b in all the consecutive TS1 Ordered Sets if the current data rate is 8.0 GT/s or
higher.
o If the Extended Synch bit is Set, the Transmitter must send a minimum of 1024
30 consecutive TS1 Ordered Sets before transitioning to Recovery.RcvrCfg.
o If this substate was entered from Recovery.Equalization, the Upstream Port must
evaluate the equalization coefficients or preset received by all Lanes that receive eight
TS1 Ordered Sets and note whether they are different from the final set of coefficients
or preset that was accepted in Phase 2 of the equalization process. Note: Mismatches are
35 reported in Recovery.RcvrCfg by setting the Request Equalization bit of TS2 Ordered
Sets.
 Otherwise, after a 24 ms timeout:
o Next state is Recovery.RcvrCfg if the following two conditions are true:
 Eight consecutive TS1 or TS2 Ordered Sets are received on any configured Lane
40 with the same Link and Lane numbers that match what is being transmitted on
the same Lane and the speed_change bit equal to 1b.
PCI Express Base Specification, Rev. 4.0 Version 1.0
324
 Either the current data rate of operation is greater than 2.5 GT/s; or 5.0 GT/s or
greater data rate identifiers are set in both the transmitted TS1 and the (eight
consecutive) received TS1 or TS2 Ordered Sets.
o Else the next state is Recovery.Speed if the speed of operation has not changed to a
mutually negotiated data rate since entering Recovery 5 from L0 or L1 (i.e.,
changed_speed_recovery = 0b) and the current speed of operation is greater than 2.5
GT/s. The new data rate to operate after leaving Recovery.Speed will be at 2.5 GT/s.
Note: This indicates that the Link was unable to operate at the current data rate (greater
than 2.5 GT/s) and the Link will operate at the 2.5 GT/s data rate.
10 o Else the next state is Recovery.Speed if the operating speed has been changed to a
mutually negotiated data rate since entering Recovery from L0 or L1
(changed_speed_recovery = 1b; i.e., the arc to this substate has been taken from
Recovery.Speed). The new data rate to operate after leaving Recovery.Speed is reverted
back to the speed it was when Recovery was entered from L0 or L1.
15 Note: This indicates that the Link was unable to operate at the new negotiated data rate
and will revert back to the old data rate with which it entered Recovery from L0 or L1.
o Else the next state is Configuration and the directed_speed_change variable is reset to 0b
if any of the configured Lanes that are receiving a TS1 or TS2 Ordered Set have received
at least one TS1 or TS2 Ordered Set with Link and Lane numbers that match what is
20 being transmitted on those same Lanes and the operating speed has not changed to a
mutually negotiated data rate (i.e., changed_speed_recovery = 0b) since entering
Recovery and at least one of the following conditions is true:
 The directed_speed_change variable is equal to 0b and the speed_change bit on
the received TS1 or TS2 Ordered Set is equal to 0b.
25  The current data rate of operation is 2.5 GT/s and 2.5 GT/s data rate is the
highest commonly advertised data rate among the transmitted TS1 Ordered Sets
and the received TS1 or TS2 Ordered Set(s).
o Otherwise, the next state is Detect.
PCI Express Base Specification, Rev. 4.0 Version 1.0
325
IMPLEMENTATION NOTE
Example Showing Speed Change Algorithm Between 2.5 GT/s and
5.0 GT/s
Suppose a Link connects two greater than 5.0 GT/s capable components, A and B. The Link
comes up to the L0 state in 2.5 GT/s data rate. Component A decides t 5 o change the speed to
greater than 5.0 GT/s, sets the directed_speed_change variable to 1b and enters Recovery.RcvrLock
from L0. Component A sends TS1 Ordered Sets with the speed_change bit set to 1b and advertises
the 2.5 GT/s, 5.0 GT/s, and 8.0 GT/s data rates. Component B sees the first TS1 in L0 state and
enters Recovery.RcvrLock state. Initially, component B sends TS1s with the speed_change set to
10 0b. Component B will start sending the speed_change indication in its TS1 after it receives eight
consecutive TS1 Ordered Sets from component A and advertises all of the data rates it can support.
Component B will enter Recovery.RcvrCfg from where it will enter Recovery.Speed. Component A
will wait for eight consecutive TS1/TS2 with speed_change bit set from component B before
moving to Recovery.RcvrCfg and on to Recovery.Speed. Both component A and component B
15 enter Recovery.Speed and record 8.0 GT/s as the maximum speed they can operate with. The
directed_speed_change variable will be reset to 0b when in Recovery.Speed. When they enter
Recovery.RcvrLock from Recovery.Speed, they will operate at 8.0 GT/s and send TS1s with
speed_change set to 0b. If both sides work well at 8.0 GT/s, they will continue on to
Recovery.RcvrCfg and enter L0 through Recovery.Idle at 8.0 GT/s. However, if component B fails
20 to achieve Symbol lock, it will timeout in Recovery.RcvrLock and enters Recovery.Speed.
Component A would have moved on to Recovery.RcvrCfg but would see the Electrical Idle after
receiving TS1s at 8.0 GT/s after component B enters Recovery.Speed. This will cause component
A to move to Recovery.Speed. After entering Recovery.Speed for the second time, both sides will
revert back to the speed they operated with prior to entering the Recovery state (2.5 GT/s). Both
25 sides will enter L0 from Recovery in 2.5 GT/s. Component A may initiate the
directed_speed_change variable for a second time, requesting 8.0 GT/s data rate in its Data Rate
Identifier, go through the same steps, fail to establish the 8.0 GT/s data rate and go back to L0 in
2.5 GT/s data rate. On the third attempt, however, component A may decide to only advertise
2.5 GT/s and 5.0 GT/s data rates and successfully establish the Link at 5.0 GT/s data rate and enter
30 L0 at that speed. However, if either side entered Detect, that side should advertise all of the data
rates it can support, since there may have been a hot plug event.
PCI Express Base Specification, Rev. 4.0 Version 1.0
326
4.2.6.4.2 Recovery.Equalization
Transmitter sends TS1 Ordered Sets on all configured Lanes using the same Link and Lane numbers
that were set after leaving Configuration.
4.2.6.4.2.1 Downstream Lanes
5 Upon entry to this substate:
 Current phase is Phase 1
o If the data rate of operation is 8.0 GT/s:
 The Equalization 8.0 GT/s Phase 1 Successful, Equalization 8.0 GT/s Phase 2
Successful, Equalization 8.0 GT/s Phase 3 Successful, Link Equalization Request
10 8.0 GT/s, and Equalization 8.0 GT/s Complete bits of the Link Status 2 register
and the Perform Equalization bit of the Link Control 3 register are all set to 0b
 The equalization_done_8GT_data_rate variable is set to 1b
o If the data rate of operation is 16.0 GT/s:
 The Equalization 16.0 GT/s Phase 1 Successful, Equalization 16.0 GT/s Phase 2
15 Successful, Equalization 16.0 GT/s Phase 3 Successful, Link Equalization
Request 16.0 GT/s, and Equalization 16.0 GT/s Complete bits of the 16.0 GT/s
Status register and the Perform Equalization bit of the Link Control 3 registers
are all set to 0b
 The equalization_done_16GT_data_rate variable is set to 1b
20  The start_equalization_w_preset variable is set to 0b
4.2.6.4.2.1.1 Phase 1 of Transmitter Equalization
 Transmitter sends TS1 Ordered Sets using the Transmitter preset settings for the current data
rate of operation. In the TS1 Ordered Sets, the EC field is set to 01b, the Transmitter Preset
field of each Lane is set to the value of its corresponding Transmitter preset setting for the
25 current data rate, the FS, LF, and the Post-cursor Coefficient fields are set to values
corresponding to the Lane’s Transmitter preset field. The Transmitter preset settings, for each
configured Lane, must be chosen as follows:
1. If eight consecutive 8GT EQ TS2 Ordered Sets were received with supported Transmitter
preset values in the most recent transition through Recovery.RcvrCfg and the current data rate
30 of operation is 16.0 GT/s, the Transmitter preset value requested in the 8GT EQ TS2 Ordered
Sets must be used.
2. Else, if the Transmitter preset setting specified by the Downstream Port 8.0 GT/s Transmitter
Preset field of the Lane Equalization Control Register entry (for operation at the 8.0 GT/s data
rate) or the Downstream Port 16.0 GT/s Transmitter Preset field of the 16.0 GT/s Lane
35 Equalization Control Register entry (for operation at the 16.0 GT/s data rate) is a supported
value and is not a Reserved value, it must be used.
PCI Express Base Specification, Rev. 4.0 Version 1.0
327
Else, use an implementation specific method to choose a supported 3. Transmitter preset
setting for use.
 The Downstream Port is permitted to wait for up to 500 ns after entering Phase 1 before
evaluating received information for TS1 Ordered Sets if it needs the time to stabilize its Receiver
5 logic.
 Next phase is Phase 2 if all configured Lanes receive two consecutive TS1 Ordered Sets with
EC=01b and the Downstream Port wants to execute Phase 2 and Phase 3.
o The Receiver must complete its bit lock process and then recognize Ordered Sets within
2 ms after receiving the first bit of the first valid Ordered Set on its Receiver pin.
10 o If the data rate is 8.0 GT/s, the Equalization 8.0 GT/s Phase 1 Successful bit of the Link
Status 2 register is set to 1b.
o If the data rate is 16.0 GT/s, the Equalization 16.0 GT/s Phase 1 Successful bit of the
16.0 GT/s Status register is set to 1b.
o The LF and FS values received in the two consecutive TS1 Ordered Sets must be stored
15 for use during Phase 3, if the Downstream Port wants to adjust the Upstream Port’s
Transmitter coefficients.
 Else, next state is Recovery.RcvrLock if all configured Lanes receive two consecutive TS1
Ordered Sets with EC=01b and the Downstream Port does not want to execute Phase 2 and
Phase 3.
20 o If the data rate is 8.0 GT/s, The Equalization 8.0 GT/s Phase 1 Successful,
Equalization 8.0 GT/s Phase 2 Successful, Equalization 8.0 GT/s Phase 3 Successful,
and Equalization 8.0 GT/s Complete bits of the Link Status 2 register are set to 1b.
o If the data rate is 16.0 GT/s, The Equalization 16.0 GT/s Phase 1 Successful,
Equalization 16.0 GT/s Phase 2 Successful, Equalization 16.0 GT/s Phase 3 Successful,
25 and Equalization 16.0 GT/s Complete bits of the 16.0 GT/s Status register are set to 1b.
o Note: A transition to Recovery.RcvrLock might be used in the case where the
Downstream Port determines that Phase 2 and Phase 3 are not needed based on the
platform and channel characteristics.
 Else, next state is Recovery.Speed after a 24 ms timeout.
30 o successful_speed_negotiation is set to 0b
o If the data rate is 8.0 GT/s, the Equalization 8.0 GT/s Complete bit of the Link Status 2
register is set to 1b.
o If the data rate is 16.0 GT/s, the Equalization 16.0 GT/s Complete bit of the 16.0 GT/s
Status register is set to 1b.
35 4.2.6.4.2.1.2 Phase 2 of Transmitter Equalization
 Transmitter sends TS1 Ordered Sets with EC = 10b and the coefficient settings, set on each
Lane independently, as follows:
o If two consecutive TS1 Ordered Sets with EC=10b have been received since entering
Phase 2, or two consecutive TS1 Ordered Sets with EC=10b and a preset or set of
PCI Express Base Specification, Rev. 4.0 Version 1.0
328
coefficients (as specified by the Use Preset bit) different than the last two consecutive
TS1 Ordered Sets with EC=10b:
 If the preset or coefficients requested in the most recent two consecutive TS1
Ordered Sets are legal and supported (see Section 4.2.3):
• Change the transmitter settings to the requested preset 5 or coefficients
such that the new settings are effective at the Transmitter pins within 500
ns of when the end of the second TS1 Ordered Set requesting the new
setting was received at the Receiver pin. The change of Transmitter
settings must not cause any illegal voltage level or parameter at the
10 Transmitter pin for more than 1 ns.
• In the transmitted TS1 Ordered Sets, the Transmitter Preset field is set to
the requested preset (for a preset request), the Pre-cursor, Cursor, and
Post-cursor Coefficient fields are set to the Transmitter settings (for a
preset or a coefficients request), and the Reject Coefficient Values bit is
15 Clear.
 Else (the requested preset or coefficients are illegal or unsupported): Do not
change the Transmitter settings used, but reflect the requested preset or
coefficient values in the transmitted TS1 Ordered Sets and set the Reject
Coefficient Values bit to 1b.
20 o Else: the preset and coefficients currently being used by the Transmitter.
 Next phase is Phase 3 if all configured Lanes receive two consecutive TS1 Ordered Sets with
EC=11b.
o If the data rate is 8.0 GT/s, the Equalization 8.0 GT/s Phase 2 Successful bit of the Link
Status 2 register is set to 1b.
25 o If the data rate is 16.0 GT/s, the Equalization 16.0 GT/s Phase 2 Successful bit of the
16.0 GT/s Status register is set to 1b.
 Else, next state is Recovery.Speed after a 32 ms timeout with a tolerance of -0 ms and +4 ms
o successful_speed_negotiation is set to 0b.
o If the data rate is 8.0 GT/s, The Equalization 8.0 GT/s Complete bit of the Link Status
30 2 register is set to 1b.
o If the data rate is 16.0 GT/s, The Equalization 16.0 GT/s Complete bit of the 16.0
GT/s Status register is set to 1b.
4.2.6.4.2.1.3 Phase 3 of Transmitter Equalization
 Transmitter sends TS1 Ordered Sets with EC = 11b
35  The Port must evaluate and arrive at the optimal settings independently on each Lane. To
evaluate a new preset or coefficient setting that is legal, as per the rules in Section 4.2.3 and
Chapter 8:
o Request a new preset by setting the Transmitter Preset field to the desired value and set
the Use Preset bit to 1b. Or, request a new set of coefficients by setting the Pre-cursor,
PCI Express Base Specification, Rev. 4.0 Version 1.0
329
Cursor, and Post-Cursor Coefficient fields to the desired values and set the Use Preset
bit to 0b. Once a request is made, it must be continuously requested for at least 1 μs or
until the evaluation of the request is completed, whichever is later.
o Wait for the required time (500 ns plus the roundtrip delay including the logic delays
through the Downstream Port) to ensure that, if accepted, 5 the Upstream Port is
transmitting using the requested settings. Obtain Block Alignment and then evaluate the
incoming Ordered Sets. Note: The Downstream Port may simply ignore anything it
receives during this waiting period as the incoming bit stream may be illegal during the
transition to the requested settings. Hence the requirement to validate Block Alignment
10 after this waiting period. If Block Alignment cannot be obtained after an implementation
specific amount of time (in addition to the required waiting period specified above) it is
recommended to proceed to perform receiver evaluation on the incoming bit stream
regardless.
o If two consecutive TS1 Ordered Sets are received with the Transmitter Preset field (for a
15 preset request) or the Pre-cursor, Cursor, and Post-Cursor fields (for a coefficients
request) identical to what was requested and the Reject Coefficient Values bit is Clear,
then the requested setting was accepted and, depending on the results of receiver
evaluation, can be considered as a candidate final setting.
o If two consecutive TS1 Ordered Sets are received with the Transmitter Preset field (for a
20 preset request) or the Pre-cursor, Cursor, and Post-Cursor fields (for a coefficients
request) identical to what was requested and the Reject Coefficient Values bit is Set, then
the requested setting was rejected and must not be considered as a candidate final
setting.
o If, after an implementation specific amount of time following the start of receiver
25 evaluation, no consecutive TS1s with the Transmitter Preset field (for a preset request)
or the Pre-Cursor, Cursor, and Post-Cursor fields (for a coefficients request) identical to
what was requested are received, then the requested setting must not be considered as a
candidate final setting.
o The Downstream Port is responsible for setting the Reset EIEOS Interval Count bit in
30 the TS1 Ordered Sets it transmits according to its evaluation criteria and requirements.
The Use Preset bit of the received TS1 Ordered Sets must not be used to determine
whether a request is accepted or rejected.
IMPLEMENTATION NOTE
35 Reset EIEOS and Coefficient/ Preset Requests
A Port may set Reset EIEOS Interval Count to 1b when it wants a longer PRBS pattern and
subsequently clear it when it needs to obtain Block Alignment.
All TS1 Ordered Sets transmitted in this Phase are requests. The first request maybe a new preset or
a new coefficient request or a request to maintain the current link partner transmitter settings by
40 reflecting the settings received in the two consecutive TS1 Ordered Sets with EC=11b that cause the
transition to Phase 3.
PCI Express Base Specification, Rev. 4.0 Version 1.0
330
o The total amount of time spent per preset or coefficients request from transmission of
the request to the completion of the evaluation must be less than 2 ms. Implementations
that need a longer evaluation time at the final stage of optimization may continue
requesting the same preset or coefficient setting beyond the 2 ms limit but must adhere
to the 24 ms timeout in this Phase and must not take this 5 exception more than two
times. If the requester is unable to receive Ordered Sets within the timeout period, it may
assume that the requested setting does not work in that Lane.
o All new preset or coefficient settings must be presented on all configured Lanes
simultaneously. Any given Lane is permitted to continue to transmit the current preset or
10 coefficients as its new value if it does not want to change the setting at that time.
 If the data rate of operation is 8.0 GT/s:
o Next state is Recovery.RcvrLock if all configured Lanes are operating at their optimal
settings.
15 o The Equalization 8.0 GT/s Phase 3 Successful and Equalization 8.0 GT/s Complete bits
of the Link Status 2 register are set to 1b.Else, next state is Recovery.Speed after a
timeout of 24 ms with a tolerance of -0 ms and +2 ms
 successful_speed_negotiation is set to 0b
 The Equalization 8.0 GT/s Complete bit of the Link Status 2 register is set to
20 1b.
 If the data rate of operation is 16.0 GT/s:
o Next state is Recovery.RcvrLock if all configured Lanes are operating at their optimal
settings and all Lanes receive two consecutive TS1 Ordered Sets with the Retimer
Equalization Extend bit set to 0b.
25  The Equalization 16.0 GT/s Phase 3 Successful and Equalization 16.0 GT/s
Complete bits of the 16.0 GT/s Status register are set to 1b
o Else, next state is Recovery.Speed after a timeout of 24 ms with a tolerance of -0 ms and
+2 ms
 successful_speed_negotiation is set to 0b
30  The Equalization 16.0 GT/s Complete bit of the 16.0 GT/s Status register is set
to 1b.
4.2.6.4.2.2 Upstream Lanes
Upon entry to this substate:
 Current phase is Phase 0
35 o If the data rate of operation is 8.0 GT/s:
 The Equalization 8.0 GT/s Phase 1 Successful, Equalization 8.0 GT/s Phase 2
Successful, Equalization 8.0 GT/s Phase 3 Successful, Link Equalization Request
PCI Express Base Specification, Rev. 4.0 Version 1.0
331
8.0 GT/s, and Equalization 8.0 GT/s Complete bits of the Link Status 2 register
are all set to 0b
 The equalization_done_8GT_data_rate variable is set to 1b
o If the data rate of operation is 16.0 GT/s:
 The Equalization 16.0 GT/s Phase 1 Successful, Equalization 5 16.0 GT/s Phase 2
Successful, Equalization 16.0 GT/s Phase 3 Successful, Link Equalization
Request 16.0 GT/s, and Equalization 16.0 GT/s Complete bits of the 16.0
GT/s Status register are all set to 0b
 The equalization_done_16GT_data_rate variable is set to 1b
10  The start_equalization_w_preset variable is set to 0b.
4.2.6.4.2.2.1Phase 0 of Transmitter Equalization
 If the current data rate of operation is 8.0 GT/s, transmitter sends TS1 Ordered Sets using the
Transmitter settings specified by the Transmitter Preset field received in the EQ TS2 Ordered
Sets during the most recent transition to 8.0 GT/s data rate from 2.5 GT/s or 5.0 GT/s data
15 rate. If the current data rate of operation is 16.0 GT/s, transmitter sends TS1 Ordered Sets using
the 16.0 GT/s Transmitter settings specified by the Transmitter Preset field received in the 8GT
EQ TS2 Ordered Sets during the most recent transition to 16.0 GT/s data rate from 8.0 GT/s
data rate. Lanes that received a Reserved or unsupported Transmitter preset value must use an
implementation specific method to choose a supported Transmitter Preset for use. Any
20 reference to Transmitter Preset field received in EQ TS2 Ordered Sets or 16.0 GT/s
Transmitter Preset field in 8GT EQ TS2 Ordered Sets (depending on the Data Rate) for the
remainder of the Recovery.Equalization state is in reference to the presets determined above. In
the TS1 Ordered Sets, the EC field is set to 00b, the Transmitter Preset field of each Lane is set
to the value it received in the Transmitter Preset field of EQ TS2 Ordered Sets or 16.0 GT/s
25 Transmitter Preset field of 8GT EQ TS2 Ordered Sets, and the Pre-cursor Coefficient, Cursor
Coefficient, and Post-cursor Coefficient fields are set to values corresponding to the Transmitter
Preset field.
o Lanes that received a Reserved or unsupported Transmitter Preset in the EQ TS2
Ordered Sets or 8GT EQ TS2 Ordered Sets (depending on the Data Rate): In the TS1
30 Ordered Sets, the Transmitter Preset field is set to the received Transmitter Preset, the
Reject Coefficient Values bit is Set and the Coefficient fields are set to values
corresponding to the implementation-specific Transmitter Preset chosen by the Lane.58
o Lanes that did not receive EQ TS2 Ordered Sets or 8GT EQ TS2 Ordered Sets
(depending on the Data Rate): In the TS1 Ordered Sets, the Transmitter Preset field is
35 set to the implementation-specific Transmitter Preset chosen by the Lane, the Reject
Coefficient Values bit is Clear, and the Coefficient fields are set to values corresponding
58 An earlier version of this specification permitted the Reject Coefficient Values bit to be clear for this case. This is
not recommended, but is permitted.
PCI Express Base Specification, Rev. 4.0 Version 1.0
332
to the same implementation-specific Transmitter Preset chosen by the Lane and
advertised in the Transmitter Preset field.59
The Upstream Port is permitted to wait for up to 500 ns after entering  Phase 0 before evaluating
receiver information for TS1 Ordered Sets if it needs the time to stabilize its Receiver logic.
5  Next phase is Phase 1 if all the configured Lanes receive two consecutive TS1 Ordered Sets with
EC=01b.
o The Receiver must complete its bit lock process and then recognize Ordered Sets within
2 ms after receiving the first bit of the first valid Ordered Set on its Receiver pin.
o The LF and FS values received in the two consecutive TS1 Ordered Sets must be stored
10 for use during Phase 2 if the Upstream Port wants to adjust the Downstream Port’s
Transmitter coefficients.
 Else, next state is Recovery.Speed after a 12 ms timeout.
o successful_speed_negotiation is set to 0b
o If the data rate is 8.0 GT/s, the Equalization 8.0 GT/s Complete bit of the Link Status 2
15 register is set to 1b.
o If the data rate is 16.0 GT/s, the Equalization 16.0 GT/s Complete bit of the 16.0 GT/s
Status register is set to 1b.
4.2.6.4.2.2.2 Phase 1 of Transmitter Equalization
 Transmitter sends TS1 Ordered Sets using the Transmitter settings determined in Phase 0. In
20 the TS1 Ordered Sets, the EC field is set to 01b, and the FS, LF, and Post-cursor Coefficient
fields of each Lane are set to values corresponding to the Lane's current Transmitter settings.
 Next phase is Phase 2 if all configured Lanes receive two consecutive TS1 Ordered Sets with
EC=10b
o If the data rate is 8.0 GT/s, the Equalization 8.0 GT/s Phase 1 Successful bit of the Link
25 Status 2 register are set to 1b.
o If the data rate is 16.0 GT/s, the Equalization 16.0 GT/s Phase 1 Successful bit of the
16.0 GT/s Status register is set to 1b.
 Next state is Recovery.RcvrLock if all configured Lanes receive eight consecutive TS1 Ordered
Sets with EC=00b
30 o o If the data rate is 8.0 GT/s, the Equalization 8.0 GT/s Phase 1 Successful and
Equalization 8.0 GT/s Complete bits of the Link Status 2 register are set to 1b
o If the data rate is 16.0 GT/s, the Equalization 16.0 GT/s Phase 1 Successful and
Equalization 16.0 GT/s Complete bits of the 16.0 GT/s Status register are set to 1b.
 Else, next state is Recovery.Speed after a 12 ms timeout
35 o successful_speed_negotiation is set to 0b
59 An earlier version of this specification permitted the Transmitter Preset field to be undefined and the Reject
Coefficient Values bit to be clear for this case. This is not recommended, but is permitted
PCI Express Base Specification, Rev. 4.0 Version 1.0
333
o If the data rate is 8.0 GT/s, the Equalization 8.0 GT/s Complete bit of the Link Status 2
register for the current data rate of operation is set to 1b.
o If the data rate is 16.0 GT/s, the Equalization 16.0 GT/s Complete bit of the 16.0
GT/s Status register is set to 1b.
5 4.2.6.4.2.2.3Phase 2 of Transmitter Equalization
 Transmitter sends TS1 Ordered Sets with EC = 10b
 The Port must evaluate and arrive at the optimal settings independently on each Lane. To
evaluate a new preset or coefficient setting that is legal, as per the rules in Section 4.2.3 and
Chapter 8:
10 o Request a new preset by setting the Transmitter Preset field to the desired value and set
the Use Preset bit to 1b. Or, request a new set of coefficients by setting the Pre-cursor,
Cursor, and Post-cursor Coefficient fields to the desired values and set the Use Preset bit
to 0b. Once a request is made, it must be continuously requested for at least 1 μs or until
the evaluation of the request is completed, whichever is later.
15 o Wait for the required time (500 ns plus the roundtrip delay including the logic delays
through the Upstream Port) to ensure that, if accepted, the Downstream Port is
transmitting using the requested settings. Obtain Block Alignment and then evaluate the
incoming Ordered Sets. Note: The Upstream Port may simply ignore anything it receives
during this waiting period as the incoming bit stream may be illegal during the transition
20 to the requested settings. Hence the requirement to validate Block Alignment after this
waiting period. If Block Alignment cannot be obtained after an implementation specific
amount of time (in addition to the required waiting period specified above) it is
recommended to proceed to perform receiver evaluation on the incoming bit stream
regardless.
25 O If two consecutive TS1 Ordered Sets are received with the Transmitter Preset field (for a
preset request) or the Pre-cursor, Cursor, and Post-Cursor fields (for a coefficients
request) identical to what was requested and the Reject Coefficient Values bit is Clear,
then the requested setting was accepted and and, depending on the results of receiver
evaluation, can be considered as a candidate final setting..
30 O If two consecutive TS1 Ordered Sets are received with the Transmitter Preset field (for a
preset request) or the Pre-Cursor, Cursor, and Post-Cursor fields (for a coefficients
request) identical to what was requested and the Reject Coefficient Values bit is Set, then
the requested setting was rejected and must not be considered as a candidate final
setting.
35 o If, after an implementation specific amount of time following the start of receiver
evaluation, no consecutive TS1s with the Transmitter Preset field (for a preset request)
or the Pre-Cursor, Cursor, and Post-Cursor fields (for a coefficients request) identical to
what was requested are received, then the requested setting must not be considered as a
candidate final setting.
40 O The Upstream Port is responsible for setting the Reset EIEOS Interval Count bit in the
TS1 Ordered Sets it transmits according to its evaluation criteria and requirements. The
PCI Express Base Specification, Rev. 4.0 Version 1.0
334
Use Preset bit of the received TS1 Ordered Sets must not be used to determine whether
a request is accepted or rejected.
IMPLEMENTATION NOTE
Reset EIEOS and Coefficient/Preset Requests
A Port may set Reset EIEOS Interval Count to 1b when i 5 t wants a longer PRBS pattern and
subsequently clear it when it needs to obtain Block Alignment.
All TS1 Ordered Sets transmitted in this Phase are requests. The first request maybe a new preset or
a new coefficient request or a request to maintain the current link partner transmitter settings by
reflecting the settings received in the two consecutive TS1 Ordered Sets with EC=10b that cause the
10 transition to Phase 2.
o The total amount of time spent per preset or coefficients request from transmission of
the request to the completion of the evaluation must be less than 2 ms. Implementations
that need a longer evaluation time at the final stage of optimization may continue
requesting the same setting beyond the 2 ms limit but must adhere to the 24 ms timeout
15 in this Phase and must not take this exception more than two times. If the requester is
unable to receive Ordered Sets within the timeout period, it may assume that the
requested setting does not work in that Lane.
o All new preset or coefficient settings must be presented on all configured Lanes
simultaneously. Any given Lane is permitted to continue to transmit the current preset or
20 coefficients as its new value if it does not want to change the setting at that time.
 If the data rate of operation is 8.0 GT/s:
o Next phase is Phase 3 if all configured Lanes are operating at their optimal settings.
 The Equalization 8.0 GT/s Phase 2 Successful bit of the Link Status 2 register is
set to 1b
25 o Else, next state is Recovery.Speed after a 24 ms timeout with a tolerance of -0 ms and
+2 ms
 successful_speed_negotiation is set to 0b
 The Equalization 8.0 GT/s Complete bit of the Link Status 2 register is set to
1b.
30  If the data rate of operation is 16.0 GT/s:
o Next phase is Phase 3 if all configured Lanes are operating at their optimal settings and
all Lanes receive two consecutive TS1 Ordered Sets with the Retimer Equalization
Extend bit set to 0b.
 The Equalization 16.0 GT/s Phase 2 Successful bit of the 16.0 GT/s Status
35 register is set to 1b
o Else, next state is Recovery.Speed after a 24 ms timeout with a tolerance of -0 ms and
+2 ms
PCI Express Base Specification, Rev. 4.0 Version 1.0
335
 successful_speed_negotiation is set to 0b
 The Equalization 16.0 GT/s Complete bit of the 16.0 GT/s Status register is set
to 1b.
4.2.6.4.2.2.4Phase 3 of Transmitter Equalization
5  Transmitter sends TS1 Ordered Sets with EC = 11b and the coefficient settings, set on each
configured Lane independently, as follows:
o If two consecutive TS1 Ordered Sets with EC=11b have been received since entering
Phase 3, or two consecutive TS1 Ordered Sets with EC=11b and a preset or set of
coefficients (as specified by the Use Preset bit) different than the last two consecutive
10 TS1 Ordered Sets with EC=11b:
 If the preset or coefficients requested in the most recent two consecutive TS
Ordered Sets are legal and supported (see Section 4.2.3 and Chapter 8):
• Change the transmitter settings to the requested preset or coefficients
such that the new settings are effective at the Transmitter pins within 500
15 ns of when the end of the second TS1 Ordered Set requesting the new
setting was received at the Receiver pin. The change of Transmitter
settings must not cause any illegal voltage level or parameter at the
Transmitter pin for more than 1 ns.
• In the transmitted TS1 Ordered Sets, the Transmitter Preset field is set to
20 the requested preset (for a preset request), the Pre-cursor, Cursor, and
Post-cursor Coefficient fields are set to the Transmitter settings (for a
preset or a coefficients request), and the Reject Coefficient Values bit is
Clear.
 Else (the requested preset or coefficients are illegal or unsupported): Do not
25 change the Transmitter settings used, but reflect the requested preset or
coefficient values in the transmitted TS1 Ordered Sets and set the Reject
Coefficient Values bit to 1b.
o Else: the preset and coefficients currently being used by the Transmitter.
 The Transmitter preset value initially transmitted on entry to Phase 3 can be the
30 Transmitter preset value transmitted in Phase 0 for the same Data Rate or the
Transmitter preset setting currently being used by the Transmitter.
 Next state is Recovery.RcvrLock if all configured Lanes receive two consecutive TS1 Ordered
Sets with EC=00b.
o If the data rate is 8.0 GT/s, the Equalization 8.0 GT/s Phase 3 Successful and
35 Equalization 8.0 GT/s Complete bits of the Link Status 2 register are set to 1b.
o If the data rate is 16.0 GT/s, the Equalization 16.0 GT/s Phase 3 Successful and
Equalization 16.0 GT/s Complete bits of the 16.0 GT/s Status register are set to 1b.
 Else, next state is Recovery.Speed after a timeout of 32 ms with a tolerance of -0 ms and +4 ms
o successful_speed_negotiation is set to 0b
PCI Express Base Specification, Rev. 4.0 Version 1.0
336
o If the data rate is 8.0 GT/s, the Equalization 8.0 GT/s Complete bit of the Link Status 2
register is set to 1b.
o If the data rate is 16.0 GT/s, the Equalization 16.0 GT/s Complete bit of the 16.0 GT/s
Status register is set to 1b.
5 4.2.6.4.3 Recovery.Speed
 The Transmitter enters Electrical Idle and stays there until the Receiver Lanes have entered
Electrical Idle, and then additionally remains there for at least 800 ns on a successful speed
negotiation (i.e., successful_speed_negotiation = 1b) or at least 6 μs on an unsuccessful speed
negotiation (i.e., successful_speed_negotiation = 0b), but stays there no longer than an
10 additional 1 ms. The frequency of operation is permitted to be changed to the new data rate
only after the Receiver Lanes have entered Electrical Idle. If the negotiated data rate is
5.0 GT/s, and if operating in full swing mode, -6 dB de-emphasis level must be selected for
operation if the select_deemphasis variable is 0b and -3.5 dB de-emphasis level must be selected
for operation if the select_deemphasis variable is 1b. Note that if the link is already operating at
15 the highest data rate supported by both Ports, Recovery.Speed is executed but the data rate is
not changed.
An EIOSQ must be sent prior to entering Electrical Idle.
The DC common mode voltage is not required to be within specification.
An Electrical Idle condition exists on the Lanes if an EIOS is received on any of the configured
20 Lanes or Electrical Idle is detected/inferred as described in Section 4.2.4.3.
o On entry to this substate following a successful speed negotiation (i.e.,
successful_speed_negotiation = 1b), an Electrical Idle condition may be inferred on the
Receiver Lanes if a TS1 or TS2 Ordered Set has not been received in any configured
Lane in a time interval specified in Table 4-12. (This covers the case where the Link is
25 operational and both sides have successfully received TS Ordered Sets. Hence, a lack of
a TS1 or TS2 Ordered Set in the specified interval can be interpreted as entry to
Electrical Idle.)
o Else on entry to this substate following an unsuccessful speed negotiation (i.e.,
successful_speed_negotiation = 0b) if an exit from Electrical Idle has not been detected
30 at least once in any configured Lane in a time interval specified in Table 4-12. (This
covers the case where at least one side is having trouble receiving TS Ordered Sets that
was transmitted by the other agent, and hence a lack of exit from Electrical Idle in a
longer interval can be treated as equivalent to entry to Electrical Idle.)
 Next state is Recovery.RcvrLock after the Transmitter Lanes are no longer required to be in
35 Electrical Idle as described in the condition above.
o If this substate has been entered from Recovery.RcvrCfg following a successful speed
change negotiation (i.e., successful_speed_negotiation = 1b), the new data rate is
changed on all the configured Lanes to the highest common data rate advertised by both
sides of the Link. The changed_speed_recovery variable is set to 1b.
40 o Else if this substate is being entered for a second time since entering Recovery from L0
or L1 (i.e., changed_speed_recovery = 1b), the new data rate will be the data rate at
PCI Express Base Specification, Rev. 4.0 Version 1.0
337
which the LTSSM entered Recovery from L0 or L1. The changed_speed_recovery
variable will be reset to 0b.
o Else the new data rate will be 2.5 GT/s. The changed_speed_recovery variable remains
reset at 0b.
Note: This represents the case where the frequency of operation 5 in L0 was greater than
2.5 GT/s and one side could not operate at that frequency and timed out in
Recovery.RcvrLock the first time it entered that substate from L0 or L1.
 Next state is Detect after a 48 ms timeout.
o Note: This transition is not possible under normal conditions.
10  The directed_speed_change variable will be reset to 0b. The new data rate must be reflected in
the Current Link Speed field of the Link Status register.
o On a Link bandwidth change, if successful_speed_negotiation is set to 1b and the
Autonomous Change bit (bit 6 of Symbol 4) in the eight consecutive TS2 Ordered Sets
received while in Recovery.RcvrCfg is set to 1b or the speed change was initiated by the
15 Downstream Port for autonomous reasons (non-reliability and not due to the setting of
the Link Retrain bit), the Link Autonomous Bandwidth Status bit of the Link Status
register is set to 1b.
o Else: on a Link bandwidth change, the Link Bandwidth Management Status bit of the
Link Status register is set to 1b.
20 4.2.6.4.4 Recovery.RcvrCfg
Transmitter sends TS2 Ordered Sets on all configured Lanes using the same Link and Lane numbers
that were set after leaving Configuration. The speed_change bit (bit 7 of data rate identifier Symbol
in TS2 Ordered Set) must be set to 1b if the directed_speed_change variable is already set to 1b. The
N_FTS value in the transmitted TS2 Ordered Sets should reflect the number at the current data rate.
25 The Downstream Port must transmit EQ TS2 Ordered Sets (TS2 Ordered Sets with Symbol 6 bit 7
set to 1b) on each configured Lane with the Transmitter Preset and Receiver Preset Hint fields set to
the values specified by the Upstream 8.0 GT/s Port Transmitter Preset and the Upstream 8.0 GT/s
Port Receiver Preset Hint fields from the corresponding Lane Equalization Control Register entry if
all of the following conditions are satisfied:
30 a) The Downstream Port advertised 8.0 GT/s data rate support in Recovery.RcvrLock, and
8.0 GT/s data rate support has been advertised in the Configuration.Complete or
Recovery.RcvrCfg substates by the Upstream Port since exiting the Detect state, and eight
consecutive TS1 or TS2 Ordered Sets were received on any configured Lane prior to entry
to this substate with speed_change bit set to 1b
35 b) The equalization_done_8GT_data_rate variable is 0b or if directed
c) The current data rate of operation is 2.5 GT/s or 5.0 GT/s
The Downstream Port must transmit 8GT EQ TS2 Ordered Sets (TS2 Ordered Sets with Symbol 7
bit 7 set to 1b) on each configured Lane with the Transmitter Preset field set to the values specified
by the Upstream Port 16.0 GT/s Transmitter Preset field from the corresponding 16.0 GT/s Lane
40 Equalization Control Register entry if all of the following conditions are satisfied:
PCI Express Base Specification, Rev. 4.0 Version 1.0
338
a) The Downstream Port advertised 16.0 GT/s data rate support in Recovery.RcvrLock, and
16.0 GT/s data rate support has been advertised in the Configuration.Complete or
Recovery.RcvrCfg substates by the Upstream Port since exiting the Detect state, and eight
consecutive TS1 or TS2 Ordered Sets were received on any configured Lane prior to entry
to this substate 5 with speed_change bit set to 1b
b) The equalization_done_16GT_data_rate variable is 0b or if directed
c) The current data rate of operation is 8.0 GT/s
The Upstream Port may optionally transmit 8GT EQ TS2 Ordered Sets with the 16.0 GT/s
Transmitter Preset fields set to implementation specific values if all of the following conditions are
10 satisfied:
a) The Upstream Port advertised 16.0 GT/s data rate support in Recovery.RcvrLock, and 16.0
GT/s data rate support has been advertised in the Configuration.Complete or
Recovery.RcvrCfg substates by the Downstream Port since exiting the Detect state, and
eight consecutive TS1 or TS2 Ordered Sets were received on any configured Lane prior to
15 entry to this substate with speed_change bit set to 1b
b) The equalization_done_16GT_data_rate variable is 0b or if directed
c) The current data rate of operation is 8.0 GT/s
When using 128b/130b encoding, Upstream and Downstream Ports use the Request
Equalization, Equalization Request Data Rate, and Quiesce Guarantee bits of their transmitted
20 TS2 Ordered Sets to communicate equalization requests as described in Section 4.2.3. When not
requesting equalization, the Request Equalization, Equalization Request Data Rate, and Quiesce
Guarantee bits must be set to 0b.
The start_equalization_w_preset variable is reset to 0b upon entry to this substate.
 On entry to this substate, a Downstream Port must set the select_deemphasis variable equal to
25 the Selectable De-emphasis field in the Link Control 2 register or adopt some implementation
specific mechanism to set the select_deemphasis variable, including using the value requested by
the Upstream Port in the eight consecutive TS1 Ordered Sets it received. A Downstream Port
advertising 5.0 GT/s data rate support must set the Selectable De-emphasis bit (Symbol 4 bit 6)
of the TS2 Ordered Sets it transmits identical to the select_deemphasis variable. An Upstream
30 Port must set its Autonomous Change bit (Symbol 4 bit 6) to 1b in the TS2 Ordered Set if it
intends to change the Link bandwidth for autonomous reasons.
o For devices that support Link width upconfigure, it is recommended that the Electrical
Idle detection circuitry be activated in the set of currently inactive Lanes in this substate,
the Recovery.Idle substate, and Configuration.Linkwidth.Start substates, if the
35 directed_speed_change variable is reset to 0b. This is done so that during a Link
upconfigure, the side that does not initiate the upconfiguration does not miss the first
EIEOS sent by the initiator during the Configuration.Linkwidth.Start substate.
 Next state is Recovery.Speed if all of the following conditions are true:
o One of the following conditions is satisfied:
40 i. Eight consecutive TS2 Ordered Sets are received on any configured Lane
with identical data rate identifiers, identical values in Symbol 6, and the
PCI Express Base Specification, Rev. 4.0 Version 1.0
339
speed_change bit set to 1b and eight consecutive TS2 Ordered Sets are
standard TS2 Ordered Sets if either 8b/10b or 128b/130b encoding is used
ii. Eight consecutive EQ TS2 or 8GT EQ TS2 Ordered Sets are received on all
configured Lanes with identical data rate identifiers, identical value in Symbol
6, and the speed_5 change bit set to 1b
iii. Eight consecutive EQ TS2 or 8GT EQ TS2 Ordered Sets are received on
any configured Lane with identical data rate identifiers, identical value in
Symbol 6, and the speed_change bit set to 1b and 1 ms has expired since the
receipt of the eight consecutive EQ Ordered Sets on any configured Lane
10 o Either the current data rate is greater than 2.5 GT/s or greater than 2.5 GT/s data rate
identifiers are set both in the transmitted and the (eight consecutive) received TS2
Ordered Sets
o For 8b/10b encoding, at least 32 TS2 Ordered Sets, without being interrupted by any
intervening EIEOS, are transmitted with the speed_change bit set to 1b after receiving
15 one TS2 Ordered Set with the speed_change bit set to 1b in the same configured Lane.
For 128b/130b encoding, at least 128 TS2 Ordered Sets are transmitted with the
speed_change bit set to 1b after receiving one TS2 Ordered Set with the speed_change
bit set to 1b in the same configured Lane.
The data rate(s) advertised on the received eight consecutive TS2 Ordered Sets with the
20 speed_change bit set is noted as the data rate(s) that can be supported by the other Port. The
Autonomous Change bit (Symbol 4 bit 6) in these received eight consecutive TS2 Ordered Sets
is noted by the Downstream Port for possible logging in the Link Status register in
Recovery.Speed substate. Upstream Ports must register the Selectable De-emphasis bit (bit 6 of
Symbol 4) advertised in these eight consecutive TS2 Ordered Sets in the select_deemphasis
25 variable. The new speed to change to in Recovery.Speed is the highest data rate that can be
supported by both Ports on the Link. For an Upstream Port, if the current data rate of
operation is 2.5 GT/s or 5.0 GT/s and these eight consecutive TS2 Ordered Sets are EQ TS2
Ordered Sets, it must set the start_equalization_w_preset variable to 1b and update the
Upstream Port 8.0 GT/s Transmitter Preset and Upstream Port 8.0 GT/s Receiver Preset Hint
30 fields of the Lane Equalization Control Register entry with the values received in the eight
consecutive EQ TS2 Ordered Sets for the corresponding Lane. For an Upstream Port, if the
current data rate of operation is 8.0 GT/s, 16.0 GT/s support is advertised by both ends, and
these eight consecutive TS2 Ordered Sets are 8GT EQ TS2 Ordered Sets, it must set the
start_equalization_w_preset variable to 1b and update the 16.0 GT/s Upstream Port
35 Transmitter Preset field of the 16.0 GT/s Lane Equalization Control Register entry with the
values received in the eight consecutive 8GT EQ TS2 Ordered Sets for the corresponding Lane.
Any configured Lanes which do not receive EQ TS2 or 8GT EQ TS2 Ordered Sets meeting this
criteria will use implementation dependent preset values when first operating at 8.0 GT/s or
16.0 GT/s prior to performing link equalization. A Downstream Port must set the
40 start_equalization_w_preset variable to 1b if the equalization_done_8GT_data_rate variable is
0b or if 16.0 GT/s support is advertised by both ends and the
equalization_done_16GT_data_rate variable is 0b or if directed. A Downstream Port must
record the 16.0 GT/s Transmitter Preset settings advertised in the eight consecutive TS2
Ordered Sets received if they are 8GT EQ TS2 Ordered Sets, and 16.0 GT/s support is
45 advertised by both ends. The variable successful_speed_negotiation is set to 1b. Note that if
PCI Express Base Specification, Rev. 4.0 Version 1.0
340
the Link is already operating at the highest data rate supported by both Ports, Recovery.Speed is
executed but the data rate is not changed. If 128b/130b encoding is used and the Request
Equalization bit is Set in the eight consecutive TS2 Ordered Sets, the Port must handle it as an
equalization request as described in Section 4.2.3.
Next state is Recovery.Idle if the following two conditions 5  are both true:
o Eight consecutive TS2 Ordered Sets are received on all configured Lanes with the same
Link and Lane number that match what is being transmitted on those same Lanes with
identical data rate identifiers within each Lane and one of the following two subconditions
are true:
10  the speed_change bit is 0b in the received eight consecutive TS2 Ordered Sets
 current data rate is 2.5 GT/s and either no 5.0 GT/s, or higher, data rate
identifiers are set in the received eight consecutive TS2 Ordered Sets, or no 5.0
GT/s, or higher, data rate identifiers are being transmitted in the TS2 Ordered
Sets
15 o 16 TS2 Ordered Sets are sent after receiving one TS2 Ordered Set without being
interrupted by any intervening EIEOS. The changed_speed_recovery variable and the
directed_speed_change variable are reset to 0b on entry to Recovery.Idle.
o If the N_FTS value was changed, the new value must be used for future L0s states.
o When using 8b/10b encoding, Lane-to-Lane de-skew must be completed before leaving
20 Recovery.RcvrCfg.
o The device must note the data rate identifier advertised on any configured Lane in the
eight consecutive TS2 Ordered Sets described in this state transition. This will override
any previously recorded value.
o When using 128b/130b encoding and if the Request Equalization bit is Set in the eight
25 consecutive TS2 Ordered Sets, the device must note it and follow the rules in Section
4.2.3.
 Next state is Configuration if eight consecutive TS1 Ordered Sets are received on any configured
Lanes with Link or Lane numbers that do not match what is being transmitted on those same
Lanes and 16 TS2 Ordered Sets are sent after receiving one TS1 Ordered Set and one of the
30 following two conditions apply:
o the speed_change bit is 0b on the received TS1 Ordered Sets
o current data rate is 2.5 GT/s and either no 5.0 GT/s, or higher, data rate identifiers are
set in the received eight consecutive TS1 Ordered Sets, or no 5.0 GT/s, or higher, data
rate identifiers are being transmitted in the TS2 Ordered Sets
35 The changed_speed_recovery variable and the directed_speed_change variable are reset to 0b if
the LTSSM transitions to Configuration.
o If the N_FTS value was changed, the new value must be used for future L0s states.
 Next state is Recovery.Speed if the speed of operation has changed to a mutually negotiated data
rate since entering Recovery from L0 or L1 (i.e., changed_speed_recovery = 1b) and an EIOS
40 has been detected or an Electrical Idle condition has been inferred/detected on any of the
configured Lanes and no configured Lane received a TS2 Ordered Set since entering this
PCI Express Base Specification, Rev. 4.0 Version 1.0
341
substate (Recovery.RcvrCfg). The new data rate to operate after leaving Recovery.Speed will be
reverted back to the speed of operation during entry to Recovery from L0 or L1.
As described in Section 4.2.4.3, an Electrical Idle condition may be inferred if a TS1 or TS2
Ordered Set has not been received in a time interval specified in Table 4-12.
Next state is Recovery.Speed if the speed of operation has not changed 5  to a mutually negotiated
data rate since entering Recovery from L0 or L1 (i.e., changed_speed_recovery = 0b) and the
current speed of operation is greater than 2.5 GT/s and an EIOS has been detected or an
Electrical Idle condition has been detected/inferred on any of the configured Lanes and no
configured Lane received a TS2 Ordered Set since entering this substate (Recovery.RcvrCfg).
10 The new data rate to operate after leaving Recovery.Speed will be 2.5 GT/s.
As described in Section 4.2.4.3, an Electrical Idle condition may be inferred if a TS1 or TS2
Ordered Set has not been received in a time interval specified in Table 4-12.
Note: This transition implies that the other side was unable to achieve Symbol lock or Block
alignment at the speed with which it was operating. Hence both sides will go back to the
15 2.5 GT/s speed of operation and neither device will attempt to change the speed again without
exiting Recovery state. It should also be noted that even though a speed change is involved
here, the changed_speed_recovery will be 0b.
 After a 48 ms timeout;
o The next state is Detect if the current data rate is 2.5 GT/s or 5.0 GT/s.
20 o The next state is Recovery.Idle if the idle_to_rlock_transitioned variable is less than FFh
and the current data rate is 8.0 GT/s or higher.
i. The changed_speed_recovery variable and the directed_speed_change
variable are reset to 0b on entry to Recovery.Idle.
o Else the next state is Detect.
25 4.2.6.4.5 Recovery.Idle
 Next state is Disabled if directed.
o Note: “if directed” applies to a Downstream or optional crosslink Port that is instructed
by a higher Layer to assert the Disable Link bit (TS1 and TS2) on the Link.
 Next state is Hot Reset if directed.
30 o Note: “if directed” applies to a Downstream or optional crosslink Port that is instructed
by a higher Layer to assert the Hot Reset bit (TS1 and TS2) on the Link.
 Next state is Configuration if directed.
o Note: “if directed” applies to a Port that is instructed by a higher Layer to optionally reconfigure
the Link (i.e., different width Link).
35  Next state is Loopback if directed to this state, and the Transmitter is capable of being a
loopback master, which is determined by implementation specific means.
o Note: “if directed” applies to a Port that is instructed by a higher Layer to assert the
Loopback bit (TS1 and TS2) on the Link.
PCI Express Base Specification, Rev. 4.0 Version 1.0
342
Next state is Disabled immediately after any configured Lane has the Disable  Link bit asserted in
two consecutively received TS1 Ordered Sets.
o Note: This is behavior only applicable to Upstream and optional crosslink Ports.
 Next state is Hot Reset immediately after any configured Lane has the Hot Reset bit asserted in
5 two consecutive TS1 Ordered Sets.
o Note: This is behavior only applicable to Upstream and optional crosslink Ports.
 Next state is Configuration if two consecutive TS1 Ordered Sets are received on any configured
Lane with a Lane number set to PAD.
o Note: A Port that optionally transitions to Configuration to change the Link
10 configuration is guaranteed to send Lane numbers set to PAD on all Lanes.
o Note: It is recommended that the LTSSM initiate a Link width up/downsizing using this
transition to reduce the time it takes to change the Link width.
 Next state is Loopback if any configured Lane has the Loopback bit asserted in two consecutive
TS1 Ordered Sets.
15 o Note: The device receiving the Ordered Set with the Loopback bit set becomes the
loopback slave.
 When using 8b/10b encoding, the Transmitter sends Idle data on all configured Lanes.
 When using 128b/130b encoding:
o If the data rate is 8.0 GT/s, the Transmitter sends one SDS Ordered Set on all
20 configured Lanes to start a Data Stream and then sends Idle data Symbols on all
configured Lanes. The first Idle data Symbol transmitted on Lane 0 is the first Symbol
of the Data Stream.
o If the data rate is 16.0 GT/s, the Transmitter sends one Control SKP Ordered Set
followed immediately by one SDS Ordered Set on all configured Lanes to start a Data
25 Stream and then sends Idle data Symbols on all configured Lanes. The first Idle data
Symbol transmitted on Lane 0 is the first Symbol of the Data Stream.
o If directed to other states, Idle Symbols do not have to be sent, and must not be sent
with 128b/130b encoding, before transitioning to the other states (i.e., Disabled, Hot
Reset, Configuration, or Loopback)
30 IMPLEMENTATION NOTE
EDS Usage
In 128b/130b encoding, on transition to Configuration or Loopback or Hot Reset or Disabled, an
EDS must be sent if a Data Stream is active (i.e., an SDS Ordered Set has been sent). It is possible
that the side that is not initiating Link Upconfigure has already transmitted SDS and transmitting
35 Data Stream (Logical IDL) when it receives the TS1 Ordered Sets. In that situation, it will send EDS
in the set of Lanes that are active before sending the TS1 Ordered Sets in Configuration.
PCI Express Base Specification, Rev. 4.0 Version 1.0
343
When using 8b/10b encoding, next state is L0 if eight consecutive  Symbol Times of Idle data
are received on all configured Lanes and 16 Idle data Symbols are sent after receiving one Idle
data Symbol.
o If software has written a 1b to the Retrain Link bit in the Link Control register since the
5 last transition to L0 from Recovery or Configuration, the Downstream Port must set the
Link Bandwidth Management Status bit of the Link Status register to 1b.
10
15
20
 When using 128b/130b encoding, next state is L0 if eight consecutive Symbol Times of Idle data
are received on all configured Lanes, 16 Idle data Symbols are sent after receiving one Idle data
Symbol, and this state was not entered by a timeout from Recovery.RcvrCfg
o The Idle data Symbols must be received in Data Blocks.
o Lane-to-Lane de-skew must be completed before Data Stream processing starts.
o If software has written a 1b to the Retrain Link bit in the Link Control register since the
last transition to L0 from Recovery or Configuration, the Downstream Port must set the
Link Bandwidth Management Status bit of the Link Status register to 1b.
o The idle_to_rlock_transitioned variable is reset to 00h on transition to L0.
 Otherwise, after a 2 ms timeout:
o If the idle_to_rlock_transitioned variable is less than FFh, the next state is
Recovery.RcvrLock.
 If the data rate is 8.0 GT/s or higher, the idle_to_rlock_transitioned variable is
incremented by 1b upon transitioning to Recovery.RcvrLock.
 If the data rate is 5.0 GT/s (or, if supported in 2.5 GT/s), the
idle_to_rlock_transitioned variable is set to FFh, upon transitioning to
Recovery.RcvrLock.
PCI Express Base Specification, Rev. 4.0 Version 1.0
344
o Else the next state is Detect
Figure 4-27: Recovery Substate Machine
Exit to
Disabled
Exit to
Loopback
A-0522A
Entry
Recovery
Exit to
Detect
Exit to
L0
Exit to
Configuration
Exit to
Hot Reset
Recovery.Idle
Recovery.RcvrLock
Recovery.Speed
Recovery.RcvrCfg
PCI Express Base Specification, Rev. 4.0 Version 1.0
345
4.2.6.5 L0
This is the normal operational state.
 LinkUp = 1b (status is set true).
o On receipt of an STP or SDP Symbol, the idle_to_rlock_transitioned variable is reset to
5 00h.
 Next state is Recovery if either of the two conditions are satisfied (i) if directed to change speed
(directed_speed_change variable = 1b) by a higher layer when both sides support greater than
2.5 GT/s speeds and the Link is in DL_Active state, or (ii) if directed to change speed
(directed_speed_change variable = 1b) by a higher layer when both sides support 8.0 GT/s data
10 rate to perform Transmitter Equalization at 8.0 GT/s data rate. The changed_speed_recovery
bit is reset to 0b.
o For an Upstream Port, the directed_speed_change variable must not be set to 1b if it has
never recorded greater than 2.5 GT/s data rate support advertised in
Configuration.Complete or Recovery.RcvrCfg substates by the Downstream Port since
15 exiting the Detect state.
o For a Downstream Port, the directed_speed_change variable must not be set to 1b if it
has never recorded greater than 2.5 GT/s data rate support advertised in
Configuration.Complete or Recovery.RcvrCfg substates by the Upstream Port since
exiting the Detect state. If greater than 2.5 GT/s data rate support has been noted, the
20 Downstream Port must set the directed_speed_change variable to 1b if the Retrain Link
bit of the Link Control register is set to 1b and the Target Link Speed field in the Link
Control 2 register is not equal to the current Link speed.
o A Port supporting greater than 2.5 GT/s data rates must participate in the speed change
even if the Link is not in DL_Active state if it is requested by the other side through the
25 TS Ordered Sets.
 Next state is Recovery if directed to change Link width.
o The upper layer must not direct a Port to increase the Link width if the other Port did
not advertise the capability to upconfigure the Link width during the Configuration state
or if the Link is currently operating at the maximum possible width it negotiated on
30 initial entry to the L0 state.
o Normally, the upper layer will not reduce width if upconfigure_capable is reset to 0b
other than for reliability reasons, since the Link will not be able to go back to the original
width if upconfigure_capable is 0b. A Port must not initiate reducing the Link width for
reasons other than reliability if the Hardware Autonomous Width Disable bit in the Link
35 Control register is set to 1b.
o The decision to initiate an increase or decrease in the Link width, as allowed by the
specification, is implementation specific.
 Next state is Recovery if a TS1 or TS2 Ordered Set is received on any configured Lane or an
EIEOS is received on any configured Lane in 128b/130b encoding.
40  Next state is Recovery if directed to this state. If Electrical Idle is detected/inferred on all Lanes
without receiving an EIOS on any Lane, the Port may transition to the Recovery state or may
PCI Express Base Specification, Rev. 4.0 Version 1.0
346
remain in L0. In the event that the Port is in L0 and the Electrical Idle condition occurs without
receiving an EIOS, errors may occur and the Port may be directed to transition to Recovery.
o As described in Section 4.2.4.3, an Electrical Idle condition may be inferred on all Lanes
under any one of the following conditions: (i) absence of a Flow Control Update DLLP
in any 128 μs window, (ii) absence of a SKP Ordered S 5 et in any of the configured Lanes
in any 128 μs window, or (iii) absence of either a Flow Control Update DLLP or a SKP
Ordered Set in any of the configured Lanes in any 128 μs window.
o Note: “if directed” applies to a Port that is instructed by a higher Layer to transition to
Recovery including the Retrain Link bit in the Link Control register being set.
10 o The Transmitter may complete any TLP or DLLP in progress.
 Next state is L0s for only the Transmitter if directed to this state and the Transmitter
implements L0s. See Section 4.2.6.6.2.
o Note: “if directed” applies to a Port that is instructed by a higher Layer to initiate L0s
(see Section 5.4.1.1.1).
15 o Note: This is a point where the TX and RX may diverge into different LTSSM states.
 Next state is L0s for only the Receiver if an EIOS is received on any Lane, the Receiver
implements L0s, and the Port is not directed to L1 or L2 states by any higher layers. See
Section 4.2.6.6.1.
o Note: This is a point where the TX and RX may diverge into different LTSSM states.
20  Next state is Recovery if an EIOS is received on any Lane, the Receiver does not implement
L0s, and the Port is not directed to L1 or L2 states by any higher layers. See Section 4.2.6.6.1.
 Next state is L1:
(i) If directed
and
25 (ii) an EIOS is received on any Lane
and
(iii) an EIOSQ is transmitted on all Lanes.
o Note: “if directed” is defined as both ends of the Link having agreed to enter L1
immediately after the condition of both the receipt and transmission of the EIOS(s) is
30 met. A transition to L1 can be initiated by PCI-PM (see Section 5.3.2.1) or by ASPM
(see Section 5.4.1.2.1).
o Note: When directed by a higher Layer one side of the Link always initiates and exits to
L1 by transmitting the EIOS(s) on all Lanes, followed by a transition to Electrical Idle.60
The same Port then waits for the receipt of an EIOS on any Lane, and then immediately
35 transitions to L1. Conversely, the side of the Link that first receives the EIOS(s) on any
Lane must send an EIOS on all Lanes and immediately transition to L1.
60 The common mode being driven must meet the Absolute Delta Between DC Common Mode During L0 and
Electrical Idle (VTX-CM-DC-ACTIVE-IDLE-DELTA) specification (see Table 8-7).
PCI Express Base Specification, Rev. 4.0 Version 1.0
347
 Next state is L2:
(i) If directed
and
(ii) an EIOS is received on any Lane
5 (iii) an EIOSQ is transmitted on all Lanes.
o Note: “if directed” is defined as both ends of the Link having agreed to enter L2
immediately after the condition of both the receipt and transmission of the EIOS(s) is
met (see Section 5.3.2.3 for more details).
o Note: When directed by a higher Layer, one side of the Link always initiates and exits to
10 L2 by transmitting EIOS on all Lanes followed by a transition to Electrical Idle.61 The
same Port then waits for the receipt of EIOS on any Lane, and then immediately
transitions to L2. Conversely, the side of the Link that first receives an EIOS on any
Lane must send an EIOS on all Lanes and immediately transition to L2.
4.2.6.6 L0s
15 The L0s substate machine is shown in Figure 4-28.
4.2.6.6.1 Receiver L0s
A Receiver must implement L0s if its Port advertises support for L0s, as indicated by the ASPM
Support field in the Link Capabilities register. It is permitted for a Receiver to implement L0s even
if its Port does not advertise support for L0s.
20 4.2.6.6.1.1 Rx_L0s.Entry
 Next state is Rx_L0s.Idle after a TTX-IDLE-MIN (Table 8-3) timeout.
o Note: This is the minimum time the Transmitter must be in an Electrical Idle condition.
4.2.6.6.1.2 Rx_L0s.Idle
 Next state is Rx_L0s.FTS if the Receiver detects an exit from Electrical Idle on any Lane of the
25 configured Link.
 Next state is Rx_L0s.FTS after a 100 ms timeout if the current data rate is 8.0 GT/s or higher
and the Port's Receivers do not meet the ZRX-DC specification for 2.5 GT/s (see Table 8-11). All
Ports are permitted to implement the timeout and transition to Rx_L0s.FTS when the data rate
is 8.0 GT/s or higher.
61 The common mode being driven does not need to meet the Absolute Delta Between DC Common Mode During
L0 and Electrical Idle (VTX-CM-DC-ACTIVE-IDLE-DELTA) specification (see Table 8-7).
PCI Express Base Specification, Rev. 4.0 Version 1.0
348
4.2.6.6.1.3 Rx_L0s.FTS
The next state is L0 if a SKP Ordered Set is received in 8b/10b encoding  or the SDS Ordered
Set is received for 128b/130b encoding on all configured Lanes of the Link.
o The Receiver must be able to accept valid data immediately after the SKP Ordered Set
5 for 8b/10b encoding.
o The Receiver must be able to accept valid data immediately after the SDS Ordered Set
for 128b/130b encoding.
o Lane-to-Lane de-skew must be completed before leaving Rx_L0s.FTS.
 Otherwise, next state is Recovery after the N_FTS timeout.
10 o When using 8b/10b encoding: The N_FTS timeout shall be no shorter than
40*[N_FTS+3] * UI (The 3 * 40 UI is derived from six Symbols to cover a maximum
SKP Ordered Set + four Symbols for a possible extra FTS + 2 Symbols of design
margin), and no longer than twice this amount. When the Extended Synch bit is Set the
Receiver N_FTS timeout must be adjusted to no shorter than 40* [2048] * UI (2048
15 FTSs) and no longer than 40* [4096] * UI (4096 FTSs). Implementations must take into
account the worst case Lane to Lane skew, their design margins, as well as the four to
eight consecutive EIE Symbols in speeds other than 2.5 GT/s when choosing the
appropriate timeout value within the specification’s defined range.
o When using 128b/130b encoding: The N_FTS timeout shall be no shorter than
20 130*[N_FTS+5+ 12 + Floor(N_FTS/32)] * UI and no longer than twice this amount.
The 5 + Floor(N_FTS/32) accounts for the first EIEOS, the last EIEOS, the SDS, the
periodic EIEOS and an additional EIEOS in case an implementation chooses to send
two EIEOS followed by an SDS when N_FTS is divisible by 32. The 12 is there to
account for the number of SKP Ordered Sets that will be transmitted if the Extended
25 Synch bit is Set. When the Extended Synch bit is Set, the timeout should be the same as
the normal case with N_FTS equal to 4096.
o The Transmitter must also transition to Recovery, but is permitted to complete any TLP
or DLLP in progress.
o It is recommended that the N_FTS field be increased when transitioning to Recovery to
30 prevent future transitions to Recovery from Rx_L0s.FTS.
4.2.6.6.2 Transmitter L0s
A Transmitter must implement L0s if its Port advertises support for L0s, as indicated by the ASPM
Support field in the Link Capabilities register. It is permitted for a Transmitter to implement L0s
even if its Port does not advertise support for L0s.
35 4.2.6.6.2.1 Tx_L0s.Entry
 Transmitter sends an EIOSQ and enters Electrical Idle.
PCI Express Base Specification, Rev. 4.0 Version 1.0
349
o The DC common mode voltage must be within specification by
TTX-IDLE-SET-TO-IDLE.62
Next state is Tx_L0s.Idle after a TTX-IDLE-MIN  (Table 8-3) timeout.
4.2.6.6.2.2 Tx_L0s.Idle
5  Next state is Tx_L0s.FTS if directed.
IMPLEMENTATION NOTE
Increase of N_FTS Due to Timeout in Rx_L0s.FTS
The Transmitter sends the N_FTS fast training sequences by going through Tx_L0s.FTS substates
to enable the Receiver to reacquire its bit and Symbol lock or Block alignment. In the absence of
10 the N_FTS fast training sequence, the Receiver will timeout in Rx_L0s.FTS substate and may
increase the N_FTS number it advertises in the Recovery state.
4.2.6.6.2.3 Tx_L0s.FTS
 Transmitter must send N_FTS Fast Training Sequences on all configured Lanes.
o Four to eight EIE Symbols must be sent prior to transmitting the N_FTS (or 4096 if the
15 Extended Synch bit is Set) number of FTS in 5.0 GT/s data rates. An EIEOS must be
sent prior to transmitting the N_FTS (or 4096 if the Extended Synch bit is Set) number
of FTS with 128b/130b encoding. In 2.5 GT/s speed, up to one full FTS may be sent
before the N_FTS (or 4096 if the Extended Synch bit is Set) number of FTSs are sent.
o SKP Ordered Sets must not be inserted before all FTSs as defined by the agreed upon
20 N_FTS parameter are transmitted.
o If the Extended Synch bit is Set, the Transmitter must send 4096 Fast Training
Sequences, inserting SKP Ordered Sets according to the requirements in Section 4.2.4.5.
 When using 8b/10b encoding, the Transmitter must send a single SKP Ordered Set on all
configured Lanes.
25  When using 128b/130b encoding, the Transmitter must send one EIEOS followed by one SDS
Ordered Set on all configured Lanes. Note: The first Symbol transmitted on Lane 0 after the
SDS Ordered Set is the first Symbol of the Data Stream.
 Next state must be L0, after completing the above required transmissions.
62 The common mode being driven must meet the Absolute Delta Between DC Common Mode During L0 and
Electrical Idle (VTX-CM-DC-ACTIVE-IDLE-DELTA) specification (see Table 8-7).
PCI Express Base Specification, Rev. 4.0 Version 1.0
350
IMPLEMENTATION NOTE
No SKP Ordered Set requirement when exiting L0s at 16.0 GT/s
Unlike in other LTSSM states, when exiting Tx_L0s.FTS no Control SKP Ordered Set is
transmitted before transmitting the SDS. This results in the Data Parity information associated with
the last portion of the previous datastream being discarded. Not sending the Control SKP Ordered
Set reduces complexity and improves exit latency.
Figure 4-28: L0s Substate Machine
PCI Express Base Specification, Rev. 4.0 Version 1.0
351
4.2.6.7 L1
The L1 substate machine is shown in Figure 4-29.
4.2.6.7.1 L1.Entry
 All configured Transmitters are in Electrical Idle.
5 o The DC common mode voltage must be within specification by
TTX-IDLE-SET-TO-IDLE.
 The next state is L1.Idle after a TTX-IDLE-MIN (Table 8-3) timeout.
o Note: This guarantees that the Transmitter has established the Electrical Idle condition.
4.2.6.7.2 L1.Idle
10  Transmitter remains in Electrical Idle.
 The DC common mode voltage must be within specification, except as allowed by L1 PM
Substates, when applicable.63
 A substate of L1 is entered when the conditions for L1 PM Substates are satisfied (see Section
5.5).
15 o The L1 PM Substate must be L1.0 when L1.Idle is entered or exited.
 Next state is Recovery if exit from Electrical Idle is detected on any Lane of a configured Link,
or directed after remaining in this substate for a minimum of 40 ns in speeds other than 2.5
GT/s.
o Ports are not required to arm the Electrical Idle exit detectors on all Lanes of the Link.
20 o Note: A minimum stay of 40 ns is required in this substate in speeds other than 2.5
GT/s to account for the delay in the logic levels to arm the Electrical Idle detection
circuitry in case the Link enters L1 and immediately exits the L1 state.
o A Port is allowed to set the directed_speed_change variable to 1b following identical
rules described in L0 for setting this variable. When making such a transition, the
25 changed_speed_recovery variable must be reset to 0b. A Port may also go through
Recovery back to L0 and then set the directed_speed_change variable to 1b on the
transition from L0 to Recovery.
o A Port is also allowed to enter Recovery from L1 if directed to change the Link width.
The Port must follow identical rules for changing the Link width as described in the L0
30 state.
 Next state is Recovery after a 100 ms timeout if the current data rate is 8.0 GT/s or higher and
the Port’s Receivers do not meet the ZRX-DC specification for 2.5 GT/s). All Ports are permitted,
63 The common mode being driven must meet the Absolute Delta Between DC Common Mode During L0 and
Electrical Idle (VTX-CM-DC-ACTIVE-IDLE-DELTA) specification (see Table 8-7).
PCI Express Base Specification, Rev. 4.0 Version 1.0
352
but not encouraged, to implement the timeout and transition to Recovery when the data rate is
8.0 GT/s or higher.
o This timeout is not affected by the L1 PM Substates mechanism.
IMPLEMENTATION NOTE
5 100 ms Timeout in L1
Ports that meet the ZRX-DC specification for 2.5 GT/s while in the L1.Idle state and are therefore not
required to implement the 100 ms timeout and transition to Recovery should avoid implementing it,
since it will reduce the power savings expected from the L1 state.
10 Figure 4-29: L1 Substate Machine
4.2.6.8 L2
The L2 substate machine is shown in Figure 4-30.
4.2.6.8.1 L2.Idle
 All Receivers must meet the ZRX-DC specification for 2.5 GT/s within 1 ms (see Table 8-11).
15  All configured Transmitters must remain in Electrical Idle for a minimum time of
TTX-IDLE-MIN.
o The DC common mode voltage does not have to be within specification.
o The Receiver needs to wait a minimum of TTX-IDLE-MIN to start looking for Electrical Idle
Exit.
PCI Express Base Specification, Rev. 4.0 Version 1.0
353
 For Downstream Lanes:
o For a Root Port, the next state is Detect if a Beacon is received on at least Lane 0 or if
directed.
 Main power must be restored before entering Detect.
5  Note: “if directed” is defined as a higher layer decides to exit to Detect.
o For a Switch, if a Beacon is received on at least Lane 0, the Upstream Port must
transition to L2.TransmitWake.
 For Upstream Lanes:
o The next state is Detect if Electrical Idle Exit is detected on any predetermined set of
10 Lanes.
 The predetermined set of Lanes must include but is not limited to any Lane
which has the potential of negotiating to Lane 0 of a Link. For multi-Lane Links
the number of Lanes in the predetermined set must be greater than or equal to
two.
15  A Switch must transition any Downstream Lanes to Detect.
o Next state is L2.TransmitWake for an Upstream Port if directed to transmit a Beacon.
 Note: Beacons may only be transmitted on Upstream Ports in the direction of
the Root Complex.
4.2.6.8.2 L2.TransmitWake
20 This state only applies to Upstream Ports.
 Transmit the Beacon on at least Lane 0.
 Next state is Detect if Electrical Idle exit is detected on any Upstream Port’s Receiver that is in
the direction of the Root Complex.
o Note: Power is guaranteed to be restored when Upstream Receivers see Electrical Idle
25 exited, but it may also be restored prior to Electrical Idle being exited.
PCI Express Base Specification, Rev. 4.0 Version 1.0
354
Figure 4-30: L2 Substate Machine
4.2.6.9 Disabled
 All Lanes transmit 16 to 32 TS1 Ordered Sets with the Disable Link bit asserted and then
5 transition to Electrical Idle.
o An EIOSQ must be sent prior to entering Electrical Idle.
o The DC common mode voltage does not have to be within specification.64
 If an EIOSQ was transmitted and an EIOS was received on any Lane (even while transmitting
TS1 with the Disable Link bit asserted), then:
10 o LinkUp = 0b (False)
 At this point, the Lanes are considered Disabled.
o For Upstream Ports: All Receivers must meet the ZRX-DC specification for 2.5 GT/s
within 1 ms (see Table 8-11).
o For Upstream Ports: The next state is Detect when Electrical Idle exit is detected on at
15 least one Lane.
 For Downstream Ports: The next state is Detect when directed (e.g., when the Link Disable bit
is reset to 0b by software).
 For Upstream Ports: If no EIOS is received after a 2 ms timeout, the next state is Detect.
4.2.6.10 Loopback
20 The Loopback substate machine is shown in Figure 4-31.
64 The common mode being driven does need to meet the Absolute Delta Between DC Common Mode During L0
and Electrical Idle (VTX-CM-DC-ACTIVE-IDLE-DELTA) specification (see Table 8-7).
PCI Express Base Specification, Rev. 4.0 Version 1.0
355
4.2.6.10.1 Loopback.Entry
 LinkUp = 0b (False)
 The Link and Lane numbers received in the TS1 or TS2 Ordered Sets are ignored by the
Receiver while in this substate.
5  Loopback master requirements:
o If Loopback.Entry was entered from Configuration.Linkwidth.Start, determine the
highest common data rate of the data rates supported by the master and the data rates
received in two consecutive TS1 or TS2 Ordered Sets on any active Lane at the time the
transition to Loopback.Entry occurred. If the current data rate is not the highest
10 common data rate:
 Transmit 16 consecutive TS1 Ordered Sets with the Loopback bit asserted,
followed by an EIOSQ, and then transition to Electrical Idle for 1 ms. During
the period of Electrical Idle, change the data rate to the highest common data
rate.
15  If the highest common data rate is 5.0 GT/s, the slave’s transmitter de-emphasis
is controlled by setting the Selectable De-emphasis bit of the transmitted TS1
Ordered Sets to the desired value (1b = -3.5 dB, 0b = -6 dB).
 For data rates of 5.0 GT/s and above, the master is permitted to choose its own
transmitter settings in an implementation-specific manner, regardless of the
20 settings it transmitted to the slave.
 Note: If Loopback is entered after LinkUp has been set to 1b, it is possible for
one Port to enter Loopback from Recovery and the other to enter Loopback
from Configuration. The Port that entered from Configuration might attempt to
change data rate while the other Port does not. If this occurs, the results are
25 undefined. The test set-up must avoid such conflicting directed clauses.
o Transmit TS1 Ordered Sets with the Loopback bit asserted.
 The master is also permitted to assert the Compliance Receive bit of TS1
Ordered Sets transmitted in Loopback.Entry, including those transmitted before
a data rate change. If it asserts the Compliance Receive bit, it must not deassert
30 it again while in the Loopback.Entry state. This usage model might be helpful
for test and validation purposes when one or both Ports have difficulty obtaining
bit lock, Symbol lock, or Block alignment after a data rate change. The ability to
set the Compliance Receive bit is implementation-specific.
o Next state is Loopback.Active after 2 ms if the Compliance Receive bit of the
35 transmitted TS1 Ordered Sets is asserted.
o Next state is Loopback.Active if the Compliance Receive bit of the transmitted TS1
Ordered Sets is deasserted and an implementation-specific set of Lanes receive two
consecutive TS1 Ordered Sets with the Loopback bit asserted.
If the data rate was changed, the master must take into account the amount of time the
40 slave can be in Electrical Idle and transmit a sufficient number of TS1 Ordered Sets for
PCI Express Base Specification, Rev. 4.0 Version 1.0
356
the slave to acquire Symbol lock or Block alignment before proceeding to
Loopback.Active.
IMPLEMENTATION NOTE
Lane Numbering with 128b/130b Encoding in Loopback
If the current data rate uses 128b/130b encoding and Lane numbers ha 5 ve not been negotiated, it is
possible that the master and slave will not be able to decode received information because their
Lanes are using different scrambling LFSR seed values (since the LFSR seed values are determined
by the Lane numbers). This situation can be avoided by allowing the master and slave to negotiate
Lane numbers before directing the master to Loopback, directing the master to assert the
10 Compliance Receive bit during Loopback.Entry, or by using some other method of ensuring that
the LFSR seed values match.
o Next state is Loopback.Exit after an implementation-specific timeout of less than 100
ms.
 Loopback slave requirements:
15 o If Loopback.Entry was entered from Configuration.Linkwidth.Start, determine the
highest common data rate of the data rates supported by the slave and the data rates
received in the two consecutive TS1 Ordered Sets that directed the slave to this state. If
the current data rate is not the highest common data rate:
 Transmit an EIOSQ, and then transition to Electrical Idle for 2 ms. During the
20 period of Electrical Idle, change the data rate to the highest common data rate.
 If operating in full swing mode and the highest common data rate is 5.0 GT/s,
set the transmitter’s de-emphasis to the setting specified by the Selectable Deemphasis
bit received in the TS1 Ordered Sets that directed the slave to this
state. The de-emphasis is -3.5 dB if the Selectable De-emphasis bit was 1b, and
25 it is -6 dB if the Selectable De-emphasis bit was 0b.
 If the highest common data rate is 8.0 GT/s or higher and EQ TS1 Ordered Sets
directed the slave to this state, set the transmitter to the settings specified by the
Preset field of the EQ TS1 Ordered Sets. See Section 4.2.3.2. If the highest
common data rate is 8.0 GT/s or higher but standard TS1 Ordered Sets directed
30 the slave to this state, the slave is permitted to use its default transmitter settings.
o Next state is Loopback.Active if the Compliance Receive bit of the TS1 Ordered Sets
that directed the slave to this state was asserted.
 The slave’s transmitter does not need to transition to transmitting looped-back
data on any boundary, and it is permitted to truncate any Ordered Set in
35 progress.
o Else, the slave transmits TS1 Ordered Sets with Link and Lane numbers set to PAD.
 Next state is Loopback.Active if the data rate is 2.5 GT/s or 5.0 GT/s and
Symbol lock is obtained on all active Lanes.
PCI Express Base Specification, Rev. 4.0 Version 1.0
357
 Next state is Loopback.Active if the data rate is 8.0 GT/s or higher and two
consecutive TS1 Ordered Sets are received on all active Lanes. The equalization
settings specified by the received TS1 Ordered Sets must be evaluated and
applied to the transmitter if the value of the EC field is appropriate for the
slave’s Port direction (10b or 11b) and the requested setting 5 is a preset or a set of
valid coefficients. (Note: This is the equivalent behavior for the
Recovery.Equalization state.) Optionally, the slave can accept both EC field
values. If the settings are applied, they must take effect within 500 ns of being
received, and they must not cause the transmitter to violate any electrical
10 specification for more than 1 ns. Unlike Recovery.Equalization, the new settings
are not reflected in the TS1 Ordered Sets that the slave transmits.
 When using 8b/10b encoding, the slave’s transmitter must transition to
transmitting looped-back data on a Symbol boundary, but it is permitted to
truncate any Ordered Set in progress. When using 128b/ 130b encoding, the
15 slave’s transmitter does not need to transition to transmitting looped-back data
on any boundary, and is permitted to truncate any Ordered Set in progress.
4.2.6.10.2 Loopback.Active
 The loopback master must send valid encoded data. The loopback master must not transmit
EIOS as data until it wants to exit Loopback. When operating with 128b/130b encoding,
20 loopback masters must follow the requirements of Section 4.2.2.5.
 A loopback slave is required to retransmit the received encoded information as received, with
the polarity inversion determined in Polling applied, while continuing to perform clock tolerance
compensation:
o SKPs must be added or deleted on a per-Lane basis as outlined in Section 4.2.7 with the
25 exception that SKPs do not have to be simultaneously added or removed across Lanes
of a configured Link.
 For 8b/10b encoding, if a SKP Ordered Set retransmission requires adding a
SKP Symbol to accommodate timing tolerance correction, the SKP Symbol is
inserted in the retransmitted Symbol stream anywhere adjacent to a SKP Symbol
30 in the SKP Ordered Set following the COM Symbol. The inserted SKP Symbol
must be of the same disparity as the received SKPs Symbol(s) in the SKP
Ordered Set.
 For 8b/10b encoding, if a SKP Ordered Set retransmission requires dropping a
SKP Symbol to accommodate timing tolerance correction, the SKP Symbol is
35 simply not retransmitted.
 For 128b/130b encoding, if a SKP Ordered Set retransmission requires adding
SKP Symbols to accommodate timing tolerance correction, four SKP Symbols
are inserted in the retransmitted Symbol stream prior to the SKP_END Symbol
in the SKP Ordered Set.
40  For 128b/130b encoding, if a SKP Ordered Set retransmission requires dropping
SKP Symbols to accommodate timing tolerance correction, four SKP Symbols
PCI Express Base Specification, Rev. 4.0 Version 1.0
358
prior to the SKP_END Symbol in the SKP Ordered Set are simply not
retransmitted.
o No modifications of the received encoded data (except for polarity inversion determined
in Polling) are allowed by the loopback slave even if it is determined to be an invalid
encoding (i.e., no legal translation to a control or data v 5 alue possible for 8b/10b
encoding or invalid Sync Header or invalid Ordered Set for 128b/130b encoding).
 Next state of the loopback slave is Loopback.Exit if one of the following conditions apply:
o If directed or if four consecutive EIOSs are received on any Lane. It must be noted that
in 8b/10b encoding, the receiving four consecutive EIOS indicates that the Lane
10 received four consecutive sets of COM, IDL, IDL, IDL or alternatively, two out of three
K28.3 (IDL) Symbols in each of the four consecutive sets of transmitted EIOS. In
128b/130b encoding, receiving four consecutive EIOS indicates receiving the full 130-
bit EIOS in the first three and the first four Symbols following a 01b Sync Header in the
last EIOS.
15 o Optionally, if current Link speed is 2.5 GT/s and an EIOS is received or Electrical Idle
is detected/inferred on any Lane.
 Note: As described in Section 4.2.4.3, an Electrical Idle condition may be
inferred if any of the configured Lanes remained electrically idle continuously for
128 μs by not detecting an exit from Electrical Idle in the entire 128 μs window.
20 o A loopback slave must be able to detect an Electrical Idle condition on any Lane within
1 ms of the EIOS being received by the loopback slave.
o Note: During the time after an EIOS is received and before Electrical Idle is actually
detected by the Loopback Slave, the Loopback Slave may receive a bit stream undefined
by the encoding scheme, which may be looped back by the transmitter.
25 o The TTX-IDLE-SET-TO-IDLE parameter does not apply in this case since the loopback slave may
not even detect Electrical Idle until as much as 1 ms after the EIOS.
 The next state of the loopback master is Loopback.Exit if directed.
4.2.6.10.3 Loopback.Exit
 The loopback master sends an EIOS for Ports that support only the 2.5 GT/s data rate and
30 eight consecutive EIOSs for Ports that support greater than 2.5 GT/s data rate, and optionally
for Ports that only support the 2.5 GT/s data rate, irrespective of the current Link speed, and
enters Electrical Idle on all Lanes for 2 ms.
o The loopback master must transition to a valid Electrical Idle condition65 on all Lanes
within TTX-IDLE-SET-TO-IDLE after sending the last EIOS.
35 o Note: The EIOS can be useful in signifying the end of transmit and compare operations
that occurred by the loopback master. Any data received by the loopback master after
any EIOS is received should be ignored since it is undefined.
65 The common mode being driven does not need to meet the Absolute Delta Between DC Common Mode During L0
and Electrical Idle (VTX-CM-DC-ACTIVE-IDLE-DELTA) specification (see Table 8-7).
PCI Express Base Specification, Rev. 4.0 Version 1.0
359
The loopback slave must enter Electrical  Idle on all Lanes for 2 ms.
o Before entering Electrical Idle the loopback slave must Loopback all Symbols that were
received prior to detecting Electrical Idle. This ensures that the loopback master may
see the EIOS to signify the logical end of any Loopback send and compare operations.
5  The next state of the loopback master and loopback slave is Detect.
Figure 4-31: Loopback Substate Machine
4.2.6.11Hot Reset
 Lanes that were directed by a higher Layer to initiate Hot Reset:
10 o All Lanes in the configured Link transmit TS1 Ordered Sets with the Hot Reset bit
asserted and the configured Link and Lane numbers.
o If two consecutive TS1 Ordered Sets are received on any Lane with the Hot Reset bit
asserted and configured Link and Lane numbers, then:
 LinkUp = 0b (False)
15  If no higher Layer is directing the Physical Layer to remain in Hot Reset, the
next state is Detect
 Otherwise, all Lanes in the configured Link continue to transmit TS1 Ordered
Sets with the Hot Reset bit asserted and the configured Link and Lane numbers.
o Otherwise, after a 2 ms timeout next state is Detect.
PCI Express Base Specification, Rev. 4.0 Version 1.0
360
Lanes that were not directed by a higher Layer to initiate Hot Reset  (i.e., received two
consecutive TS1 Ordered Sets with the Hot Reset bit asserted on any configured Lanes):
o LinkUp = 0b (False)
o If any Lane of an Upstream Port of a Switch receives two consecutive TS1 Ordered Sets
5 with the Hot Reset bit asserted, all configured Downstream Ports must transition to Hot
Reset as soon as possible.
 Any optional crosslinks on the Switch are an exception to this rule and the
behavior is system specific.
o All Lanes in the configured Link transmit TS1 Ordered Sets with the Hot Reset bit
10 asserted and the configured Link and Lane numbers.
o If two consecutive TS1 Ordered Sets were received with the Hot Reset bit asserted and
the configured Link and Lane numbers, the state continues to be Hot Reset and the 2 ms
timer is reset.
o Otherwise, the next state is Detect after a 2 ms timeout.
15 Note: Generally, Lanes of a Downstream or optional crosslink Port will be directed to Hot Reset,
and Lanes of an Upstream or optional crosslink Port will enter Hot Reset by receiving two
consecutive TS1 Ordered Sets with the Hot Reset bit asserted on any configured Lanes, from
Recovery.Idle state.
4.2.7 Clock Tolerance Compensation
20 SKP Ordered Sets (defined below) are used to compensate for differences in frequencies between
bit rates at two ends of a Link. The Receiver Physical Layer logical sub-block must include elastic
buffering which performs this compensation. The interval between SKP Ordered Set transmissions
is derived from the absolute value of the Transmit and Receive clock frequency difference specified
in Table 8-3.
25 The specification supports two kinds of clocking where the Tx and Rx Refclk rates differ. One
allows for a worst case 600 ppm difference with no SSC (Separate Reference Clocks With No SSC -
SRNS), and the other for a 5600 ppm difference for separate Refclks utilizing independent SSC
(Separate Reference Clocks with Independent SSC - SRIS) (SSC introduces a 5000 ppm difference,
and Tx/Rx crystal tolerance introduces another 600 ppm). Note that the common Refclk
30 architecture utilizes the same Refclk for Tx and Rx and so does not introduce any difference
between the Tx and Rx Refclk rates.
Specific form factor specifications are permitted to require the use of only SRIS, only SRNS, or to
provide a mechanism for clocking architecture selection. Upstream Ports are permitted to
implement support for any combination of SRIS and SRNS (including no support for either), but
35 must conform to the requirements of any associated form factor specification. Downstream Ports
supporting SRIS must also support SRNS unless the port is only associated with a specific form
factor(s) which modifies these requirements. Port configuration to satisfy the requirements of a
specific associated form factor is implementation specific.
If the clock tolerance is 600 ppm, on average, the Tx and Rx clocks can shift one clock every 1666
40 clocks. If the clock tolerance is 5600 ppm, a shift of one clock can occur every 178 clocks.
PCI Express Base Specification, Rev. 4.0 Version 1.0
361
If the receiver is capable of operating with SKP Ordered Sets being generated at the rate used in
SRNS even though the Port is running in SRIS, the Port is permitted to Set its bit for the
appropriate data rate in the Lower SKP OS Reception Supported Speeds Vector field of the Link
Capabilities 2 register. If the transmitter is capable of operating with SKP Ordered Sets being
generated at the rate used in SRNS even though the Port is running in SRIS, 5 the Port is permitted to
Set its bit for the appropriate data rate in the Lower SKP OS Generation Supported Speeds Vector
field of the Link Capabilities 2 register. System software must check that the bit is Set in the Lower
SKP OS Reception Supported Speeds Vector field before setting the appropriate data rate's bit in
the link partner’s Enable Lower SKP OS Generation Vector field of the Link Control 3 register.
10 Any software transparent extension devices (such as a repeater) present on a Link must also support
lower SKP OS Generation for system software to set the bit in the Enable Lower SKP OS
Generation Vector field. Software determination of such support in such extension devices is
implementation specific. When the bit for the data rate that the link is running in is Set in the
Enable Lower SKP OS Generation Vector field, the transmitter schedules SKP Ordered Set
15 generation in L0 at the rate used in SRNS, regardless of which clocking architecture the link is
running in. In other LTSSM states, SKP Ordered Set scheduling is at the appropriate rate for the
clocking architecture.
Components supporting SRIS may need more entries in their elastic buffers than designs supporting
SRNS only. This requirement takes into account the extra time it may take to schedule a SKP
20 Ordered Set if the latter falls immediately after a maximum payload sized packet.
4.2.7.1 SKP Ordered Set for 8b/10b Encoding
When using 8b/10b encoding, a transmitted SKP Ordered Set is a COM Symbol followed by three
SKP Symbols, except as is allowed for a Loopback Slave in the Loopback.Active LTSSM state. A
received SKP Ordered Set is a COM Symbol followed by one to five SKP Symbols. See Section
25 4.3.6.7 for Retimer rules on SKP Ordered Set modification.
4.2.7.2 SKP Ordered Set for 128b/130b Encoding
When using 128b/130b encoding, a transmitted SKP Ordered Set is 16 Symbols, and a received
SKP Ordered set can be 8, 12, 16, 20, or 24 Symbols. See Section 4.3.6.7 for Retimer rules on SKP
Ordered Set modification.
30 There are two SKP Ordered Set formats defined for 128b/130b encoding as shown in Table 4-16:
and Table 4-17. Both formats contain one to five groups of four SKP Symbols followed by a final
group of four Symbols indicated by a SKP_END or SKP_END_CTL Symbol. When operating at
8.0 GT/s, only the Standard SKP Ordered Set is used. When operating at 16.0 GT/s, both the
Standard and Control SKP Ordered Sets are used. All statements in this specification that do not
35 refer to a specific SKP Ordered Set format apply to both formats. When a SKP Ordered Set is
transmitted, all Lanes must transmit the same format of SKP Ordered Set – all Lanes must transmit
the Standard SKP Ordered Set, or all Lanes must transmit the Control SKP Ordered Set.
The Standard SKP Ordered Set contains information following the SKP_END Symbol that is based
on the LTSSM state and the sequence of Blocks. When in the Polling.Compliance state, the
40 Symbols contain the Lane’s error status information (see Section 4.2.6.2.2. for more information).
Otherwise, the Symbols contain the Lane’s scrambling LFSR value, and a Data Parity bit when the
PCI Express Base Specification, Rev. 4.0 Version 1.0
362
SKP Ordered Set follows a Data Block. The Control SKP Ordered Set contains three Data Parity
bits and additional information following the SKP_END_CTL Symbol.
When operating at 8.0 GT/s, the Data Parity bit of the Standard SKP Ordered Set is the even parity
of the payload of all Data Blocks communicated by a Lane and is computed for each Lane
independently66. Upstream and Downstream Port Transmitters compute 5 the parity as follows:
 Parity is initialized when a SDS Ordered Set is transmitted.
 Parity is updated with each bit of a Data Block’s payload after scrambling has been performed.
 The Data Parity bit of a Standard SKP Ordered Set transmitted immediately following a Data
Block is set to the current parity.
10  Parity is initialized after a Standard SKP Ordered Set is transmitted.
Upstream and Downstream Port Receivers compute and act on the parity as follows:
 Parity is initialized when a SDS Ordered Set is received.
 Parity is updated with each bit of a Data Block's payload before de-scrambling has been
performed.
15  When a Standard SKP Ordered Set is received immediately following a Data Block, each Lane
compares the received Data Parity bit to its calculated parity. If a mismatch is detected, the
receiver must set the bit of the Port's Lane Error Status register that corresponds to the Lane's
default Lane number. The mismatch is not a Receiver Error and must not cause a Link retrain.
 Parity is initialized when a Standard SKP Ordered Set is received.
20 When operating at 16.0 GT/s, the Data Parity bits of both the Standard SKP Ordered Set and the
Control SKP Ordered Set is the even parity of the payload of all Data Blocks communicated by a
Lane and is computed for each Lane independently. Upstream and Downstream Port Transmitters
compute the parity as follows:
 Parity is initialized when the LTSSM is in Recovery.Speed.
25  Parity is initialized when a SDS Ordered Set is transmitted.
 Parity is updated with each bit of a Data Block’s payload after scrambling has been performed.
 The Data Parity bit of a Standard SKP Ordered Set transmitted immediately following a Data
Block is set to the current parity.
 The Data Parity, First Retimer Data Parity, and Second Retimer Data Parity bits of a Control
30 SKP Ordered Set are all set to the current parity.
 Parity is initialized after a Control SKP Ordered Set is transmitted. However, parity is NOT
initialized after a Standard SKP Ordered Set is transmitted.
Upstream and Downstream Port Receivers compute and act on the parity as follows:
 Parity is initialized when the LTSSM is in Recovery.Speed.
35  Parity is initialized when a SDS Ordered Set is received.
66 The requirements for 8.0 GT/s operation documented here are identical to those in Revision 3.1 of the PCI
Express Base Specification.
PCI Express Base Specification, Rev. 4.0 Version 1.0
363
Parity is updated with each bit of a Data Block’s payload  before de-scrambling has been
performed.
 When a Control SKP Ordered Set is received, each Lane compares the received Data Parity bit
to its calculated parity. If a mismatch is detected, the receiver must set the bit of the Port’s
5 Local Data Parity Mismatch Status register that corresponds to the Lane’s default Lane number.
The mismatch is not a Receiver Error and must not cause a Link retrain.
 When a Control SKP Ordered Set is received, each Lane compares the received First Retimer
Data Parity bit to its calculated parity. If a mismatch is detected, the receiver must set the bit of
the Port’s First Retimer Data Parity Mismatch Status register that corresponds to the Lane’s
10 default Lane number. The mismatch is not a Receiver Error and must not cause a Link retrain.
 When a Control SKP Ordered Set is received, each Lane compares the received Second Retimer
Data Parity bit to its calculated parity. If a mismatch is detected, the receiver must set the bit of
the Port’s Second Retimer Data Parity Mismatch Status register that corresponds to the Lane’s
default Lane number. The mismatch is not a Receiver Error and must not cause a Link retrain.
15  When a Standard SKP Ordered Set is received immediately following a Data Block, the receiver
is permitted to compare the received Data Parity bit to its calculated parity bit. However, the
results of such a comparison must not affect the state of the Lane Error Status register.
 Parity is initialized when a Control SKP Ordered Set is received. However, parity is NOT
initialized when a Standard SKP Ordered Set is received.
20 See Section 4.3.6.7 for the definition of First Retimer and Second Retimer, and for Retimer Pseudo
Port requirements for parity computation and modification of the First Retimer Data Parity and
Second Retimer Data Parity bits of Control SKP Ordered Sets.
IMPLEMENTATION NOTE
LFSR in Standard SKP Ordered Set
25 The LFSR value is transmitted to enable trace tools to be able to function even if they need to
reacquire block alignment in the midst of a bit stream. Since trace tools cannot force the link to
enter Recovery, they can reacquire bit lock, if needed, and monitor for the SKP Ordered Set to
obtain Block alignment and perform Lane-to-Lane de-skew. The LFSR value from the SKP
Ordered Set can be loaded into its LFSR to start interpreting the bit stream. It must be noted that
30 with a bit stream one may alias to a SKP Ordered Set on a non-Block boundary. The trace tools can
validate their Block alignment by using implementation specific means such as receiving a fixed
number of valid packets or Sync Headers or subsequent SKP Ordered Sets.
PCI Express Base Specification, Rev. 4.0 Version 1.0
364
Table 4-16: Standard SKP Ordered Set with 128b/130b Encoding
Symbol Number Value Description
0 through (4*N - 1)
[N can be 1 through 5]
AAh SKP Symbol.
Symbol 0 is the SKP Ordered Set identifier.
4*N E1h SKP_END Symbol.
Signifies the end of the SKP Ordered Set
after three more Symbols.
4*N + 1 00-FFh (i) If LTSSM state is Polling.Compliance: AAh
(ii) Else if prior block was a Data Block:
Bit[7] = Data Parity
Bit[6:0] = LFSR[22:16]
(iii) Else:
Bit[7] = ~LFSR[22]
Bit[6:0] = LFSR[22:16]
4*N + 2 00-FFh (i) If the LTSSM state is Polling.Compliance:
Error_Status[7:0]
(ii) Else LFSR[15:8]
4*N + 3 00-FFh (i) If the LTSSM state is Polling.Compliance:
~Error_Status[7:0]
(ii) Else: LFSR[7:0]
The Control SKP Ordered Set is different from the Standard SKP Ordered Set in the last 4
Symbols. It is used to communicate the parity bits, as computed by each Retimer, 5 in addition to the
Data Parity bit computed by the Upstream/ Downstream Port. It may also be used for Lane
Margining at a Retimer’s Receiver, as described below.
Table 4-17: Control SKP Ordered Set with 128b/130b Encoding
Symbol Number Value Description
0 through (4*N - 1)
[N can be 1 through
5]
AAh SKP Symbol.
Symbol 0 is the SKP Ordered Set identifier.
4*N 78h SKP_END_CTL Symbol.
Signifies the end of the Control SKP Ordered Set after
three more Symbols.
4*N + 1 00-FFh Bit 7: Data Parity
Bit 6: First Retimer Data Parity
Bit 5: Second Retimer Parity
Bits [4:0]: Margin CRC [4:0]
4*N + 2 00-FFh Bit 7: Margin Parity
Bits [6:0]: Refer to Section 4.2.13.1
4*N + 3 00-FFh Bits [7:0]: Refer to Section 4.2.13.1
10 The ‘Margin CRC[4:0]’ is computed from Bits [6:0] in Symbols 4N+2 (referred to as d[6:0] in the
equations below, where d[0] is Bit 0 of Symbol 4N+2, d[1] is Bit 1 of Symbol 4N+2, … d[6] is Bit 6
of Symbol 4N+2) and Bits [7:0] of Symbol 4N+3 (referred to as d[14:7], where d[7] is Bit 0 of
Symbol 4N+3, d[8] is Bit 1 of Symbol 4N+3, .. d[14] is Bit 7 of Symbol 4N+3) as follows:
PCI Express Base Specification, Rev. 4.0 Version 1.0
365
Margin CRC[0] = d[0] ^ d[3] ^ d[5] ^ d[6] ^ d[9] ^ d[10] ^ d[11] ^ d[12] ^ d[13]
Margin CRC[1] = d[1] ^ d[4] ^ d[6] ^ d[7] ^ d[10] ^ d[11] ^ d[12] ^ d[13] ^ d[14]
Margin CRC[2] = d[0] ^ d[2] ^ d[3] ^ d[6] ^ d[7] ^ d[8] ^ d[9] ^ d[10] ^ d[14]
Margin CRC[3] = d[1] ^ d[3] ^ d[4] ^ d[7] ^ d[8] ^ d[9] ^ d[10] ^ d[11]
Margin CRC[4] = d[2] ^ d[4] ^ d[5] ^ 5 d[8] ^ d[9] ^ d[10] ^ d[11] ^ d[12]
’Margin Parity’ is the even parity of Bits [4:0] of Symbol 4N+1, Bits [6:0] of Symbol 4N+2, and Bits
[7:0] of Symbol 4N+3 (i.e., Margin Parity = Margin CRC[0] ^ Margin CRC[1] ^ Margin CRC[2] ^
Margin CRC[3] ^ Margin CRC[4] ^ d[0] ^ d[1] ^ d[2] ^ d[3] ^ d[4] ^ d[5] ^ d[6] ^ d[7] ^ d[8] ^ d[9] ^
d[10] ^ d[11] ^ d[12] ^ d[13] ^ d[14]).
10 The rules for generating and checking the Margin CRC and Margin Parity are described in Section
4.2.1.3.
PCI Express Base Specification, Rev. 4.0 Version 1.0
366
IMPLEMENTATION NOTE
Error Protection in Control SKP Ordered Set
The 21 bits in Symbol 4N+1 (Bits [4:0]), Symbol 4N+2 (Bits[7:0]) and Symbol 4N+3 (Bits[7:0]) is
protected by 5 bits of CRC and one bit of parity, leaving 15 bits for information passing. The parity
bit provides detection against odd number of bit-flips (e.g., 1-bit, 3 5 -bit), whereas the CRC provides
guaranteed detection of 1-bit and 2-bit flips; thus resulting in a triple bit flip detection guarantee
over the 21 bits as well as guaranteed detection of burst errors of length 5. The 5-bit CRC is derived
from the primitive polynomial: x5 + x2 + 1.
Since these 21 bits are not part of a TLP, repeated delivery of the same content provides delivery
10 guarantee. This is achieved through architected registers. Downstream commands are sent from the
Downstream Port, reflecting the contents of an architected register whereas the upstream status that
passes the error checking is updated into a status register in the Downstream Port. Software thus has
a mechanism to issue a command and wait for the status to be reflected back before issuing a new
command. Thus, these 15 bits of information act as a micro-packet.
15
4.2.7.3 Rules for Transmitters
 All Lanes shall transmit Symbols at the same frequency (the difference between bit rates is
0 ppm within all multi-Lane Links).
20  When transmitted, SKP Ordered Sets of the same length shall be transmitted simultaneously on
all Lanes of a multi-Lane Link, except as allowed for a Loopback Slave in the Loopback.Active
LTSSM State (see Section 4.2.4.10 and Table 8-3 for the definition of simultaneous in this
context).
 The transmitted SKP Ordered Set when using 8b/10b encoding must follow the definition in
25 Section 4.2.7.1.
 The transmitted SKP Ordered Set when using 128b/130b encoding must follow the definition
in Section 4.2.7.2.
 When using 8b/10b encoding:
o If the Link is not operating in SRIS, or the bit corresponding to the current Link speed is
30 Set in the Enable Lower SKP OS Generation Vector field and the LTSSM is in L0, a
SKP Ordered Set must be scheduled for transmission at an interval between 1180 and
1538 Symbol Times.
o If the Link is operating in SRIS and either the bit corresponding to the current Link
speed is Clear in the Enable Lower SKP OS Generation Vector field or the LTSSM is
35 not in L0, a SKP Ordered Set must be scheduled for transmission at an interval of less
than 154 Symbol Times.
 When using 128b/130b encoding:
o If the Link is not operating in SRIS, or the bit corresponding to the current Link speed is
Set in the Enable Lower SKP OS Generation Vector field and the LTSSM is in L0, a
PCI Express Base Specification, Rev. 4.0 Version 1.0
367
SKP Ordered Set must be scheduled for transmission at an interval between 370 and 375
Blocks. Loopback Slaves must meet this requirement until they start looping back the
incoming bit stream.
o If the Link is operating in SRIS and either the bit corresponding to the current Link
speed is Clear in the Enable Lower SKP OS Generation Vector 5 field or the LTSSM is
not in L0, a SKP Ordered Set must be scheduled for transmission at an interval less than
38 Blocks. Loopback Slaves must meet this requirement until they start looping back the
incoming bit stream.
o When the LTSSM is in the Loopback state and the Link is not operating in SRIS, the
10 Loopback Master must schedule two SKP Ordered Sets to be transmitted, at most two
Blocks apart from each other, at an interval between 370 to 375 blocks.
o When the LTSSM is in the Loopback state and the Link is operating in SRIS, the
Loopback Master must schedule two SKP Ordered Sets to be transmitted, at most two
Blocks apart from each other, at an interval of less than 38 Blocks.
15 o The Control SKP Ordered Set is transmitted only at the following times:
 When the data rate is 16.0 GT/s and transmitting a Data Stream. SKP Ordered
Sets transmitted within a Data Stream must alternate between the Standard SKP
Ordered Set and the Control SKP Ordered Set.
 When the current data rate is 16.0 GT/s and the LTSSM enters the
20 Configuration.Idle state or Recovery.Idle state. See sections 4.2.6.3.6 and
4.2.6.4.5 for more information. Transmission of this instance of the Control SKP
Ordered Set is not subject to any minimum scheduling interval requirements
described above. Transmitters are permitted, but not required, to reset their SKP
Ordered Set scheduling interval timer after transmitting this instance of the
25 Control SKP Ordered Set.
 Scheduled SKP Ordered Sets shall be transmitted if a packet or Ordered Set is not already in
progress, otherwise they are accumulated and then inserted consecutively at the next packet or
Ordered Set boundary. Note: When using 128b/130b encoding, SKP Ordered Sets cannot be
transmitted in consecutive Blocks within a Data Stream. See Section 4.2.2.3.2 for more
30 information.
 SKP Ordered Sets do not count as an interruption when monitoring for consecutive Symbols or
Ordered Sets (e.g., eight consecutive TS1 Ordered Sets in Polling.Active).
 When using 8b/10b encoding: SKP Ordered Sets must not be transmitted while the Compliance
Pattern or the Modified Compliance Pattern (see Section 4.2.8) is in progress during
35 Polling.Compliance if the Compliance SOS bit of the Link Control 2 register is 0b. If the
Compliance SOS bit of the Link Control 2 register is 1b, two consecutive SKP Ordered Sets
must be sent (instead of one) for every scheduled SKP Ordered Set time interval while the
Compliance Pattern or the Modified Compliance Pattern is in progress when using 8b/10b
encoding.
40  When using 128b/130b encoding: The Compliance SOS register bit has no effect. While in
Polling.Compliance, Transmitters must not transmit any SKP Ordered Sets other than those
specified as part of the Modified Compliance Pattern in Section 4.2.11.
PCI Express Base Specification, Rev. 4.0 Version 1.0
368
Any and all time spent in a state when the Transmitter is electrically idle  does not count in the
scheduling interval used to schedule the transmission of SKP Ordered Sets.
 It is recommended that any counter(s) or other mechanisms used to schedule SKP Ordered Sets
be reset any time when the Transmitter is electrically idle.
5 4.2.7.4 Rules for Receivers
 Receivers shall recognize received SKP Ordered Sets as defined in Section 4.2.7.1 when using
8b/10b encoding and as defined in Section 4.2.7.2 when using 128b/130b encoding.
o The length of the received SKP Ordered Sets shall not vary from Lane-to-Lane in a
multi-Lane Link, except as may occur during Loopback.Active.
10  Receivers shall be tolerant to receive and process SKP Ordered Sets at an average interval
between 1180 to 1538 Symbol Times when using 8b/10b encoding and 370 to 375 blocks when
using 128b/130b encoding when the Link is not operating in SRIS or its bit for the current Link
speed is Set in the Lower SKP OS Reception Supported Speeds Vector field. Receivers shall be
tolerant to receive and process SKP Ordered Sets at an average interval of less than 154 Symbol
15 Times when using 8b/10b encoding and less than 38 blocks when using 128b/130b encoding
when the Link is operating in SRIS.
o Note: Since Transmitters in electrical idle are not required to reset their mechanism for
time-based scheduling of SKP Ordered Sets, Receivers shall be tolerant to receive the
first time-scheduled SKP Ordered Set following electrical idle in less than the average
20 time interval between SKP Ordered Sets.
 For 8.0 GT/s and above data rates, in L0 state, Receivers must check that each SKP Ordered
Set is preceded by a Data Block with an EDS token.
 Receivers shall be tolerant to receive and process consecutive SKP Ordered Sets in 2.5 GT/s
and 5.0 GT/s data rates.
25 o Receivers shall be tolerant to receive and process SKP Ordered Sets that have a
maximum separation dependent on the Max_Payload_Size a component supports. For
2.5 GT/s and 5.0 GT/s data rates, the formula for the maximum number of Symbols
(N) between SKP Ordered Sets is: N = 1538 + (Max_payload_size_byte+28). For
example, if Max_Payload_Size is 4096 bytes, N = 1538 + 4096 + 28 = 5662.
30 4.2.8 Compliance Pattern in 8b/10b Encoding
During Polling, the Polling.Compliance substate must be entered from Polling.Active based on the
conditions described in Section 4.2.6.2.1. The compliance pattern consists of the sequence of
8b/10b Symbols K28.5, D21.5, K28.5, and D10.2 repeating. The Compliance sequence is as
follows:
35
Symbol K28.5 D21.5 K28.5 D10.2
Current Disparity Negative Positive Positive Negative
Pattern 0011111010 1010101010 1100000101 0101010101
PCI Express Base Specification, Rev. 4.0 Version 1.0
369
The first Compliance sequence Symbol must have negative disparity. It is permitted to create a
disparity error to align the running disparity to the negative disparity of the first Compliance
sequence Symbol.
For any given device that has multiple Lanes, every eighth Lane is delayed by a total of four
Symbols. A two Symbol delay occurs at both the beginning 5 and end of the four Symbol Compliance
Pattern sequence. A x1 device, or a xN device operating a Link in x1 mode, is permitted to include
the Delay Symbols with the Compliance Pattern.
This delay sequence on every eighth Lane is then:
Symbol: D D K28.5 D21.5 K28.5 D10.2 D D
10 Where D is a K28.5 Symbol. The first D Symbol has negative disparity to align the delay disparity
with the disparity of the Compliance sequence.
After the eight Symbols are sent, the delay Symbols are advanced to the next Lane, until the delay
Symbols have been sent on all eight lanes. Then the delay Symbols cycle back to Lane 0, and the
process is repeated. It is permitted to advance the delay sequence across all eight lanes, regardless of
15 the number of lanes detected or supported. An illustration of this process is shown below:
Lane 0 D D K28.5- D21.5 K28.5+ D10.2 D D K28.5- D21.5 K28.5+ D10.2
Lane 1 K28.5- D21.5 K28.5+ D10.2 K28.5- D21.5 K28.5+ D10.2 D D K28.5- D21.5
Lane 2 K28.5- D21.5 K28.5+ D10.2 K28.5- D21.5 K28.5+ D10.2 K28.5- D21.5 K28.5+ D10.2
Lane 3 K28.5- D21.5 K28.5+ D10.2 K28.5- D21.5 K28.5+ D10.2 K28.5- D21.5 K28.5+ D10.2
Lane 4 K28.5- D21.5 K28.5+ D10.2 K28.5- D21.5 K28.5+ D10.2 K28.5- D21.5 K28.5+ D10.2
Lane 5 K28.5- D21.5 K28.5+ D10.2 K28.5- D21.5 K28.5+ D10.2 K28.5- D21.5 K28.5+ D10.2
Lane 6 K28.5- D21.5 K28.5+ D10.2 K28.5- D21.5 K28.5+ D10.2 K28.5- D21.5 K28.5+ D10.2
Lane 7 K28.5- D21.5 K28.5+ D10.2 K28.5- D21.5 K28.5+ D10.2 K28.5- D21.5 K28.5+ D10.2
Lane 8 D D K28.5- D21.5 K28.5+ D10.2 D D K28.5- D21.5 K28.5+ D10.2
Lane 9 K28.5- D21.5 K28.5+ D10.2 K28.5- D21.5 K28.5+ D10.2 D D K28.5- D21.5
Key:
K28.5- COM when disparity is negative, specifically: “0011111010”
K28.5+ COM when disparity is positive, specifically: “1100000101”
D21.5 Out of phase data Symbol, specifically: “1010101010”
D10.2 Out of phase data Symbol, specifically: “0101010101”
D Delay Symbol K28.5 (with appropriate disparity)
This sequence of delays ensures interference between adjacent Lanes, enabling measurement of the
compliance pattern under close to worst-case Inter-Symbol Interference and cross-talk conditions.
PCI Express Base Specification, Rev. 4.0 Version 1.0
370
4.2.9 Modified Compliance Pattern in 8b/10b Encoding
The Modified Compliance Pattern consists of the same basic Compliance Pattern sequence (see
Section 4.2.8) with one change. Two identical error status Symbols followed by two K28.5 are
appended to the basic Compliance sequence of 8b/10b Symbols (K28.5, D21.5, K28.5, and D10.2)
to form the Modified Compliance Sequence of (K28.5, D21.5, K28.5, D 5 10.2, error status Symbol,
error status Symbol, K28.5, K28.5). The first Modified Compliance Sequence Symbol must have
negative disparity. It is permitted to create a disparity error to align the running disparity to the
negative disparity of the first Modified Compliance Sequence Symbol. For any given device that has
multiple Lanes, every eighth Lane is moved by a total of eight Symbols. Four Symbols of K28.5
10 occurs at the beginning and another four Symbols of K28.7 occurs at the end of the eight Symbol
Modified Compliance Pattern sequence. The first D Symbol has negative disparity to align the delay
disparity with the disparity of the Modified Compliance Sequence. After the 16 Symbols are sent,
the delay Symbols are advanced to the next Lane, until the delay Symbols have been sent on all eight
lanes. Then the delay Symbols cycle back to Lane 0, and the process is repeated. It is permitted to
15 advance the delay sequence across all eight lanes, regardless of the number of lanes detected or
supported. A x1 device, or a xN device operating a Link in x1 mode, is permitted to include the
Delay symbols with the Modified Compliance Pattern.
An illustration of the Modified Compliance Pattern is shown below:
Lane0 D D D D K28.5- D21.5 K28.5+ D10.2 ERR ERR K28.5- K28.5+ K28.7- K28.7- K28.7- K28.7- K28.5- D21.5
Lane1 K28.5- D21.5 K28.5+ D10.2 ERR ERR K28.5- K28.5+ K28.5- D21.5 K28.5+ D10.2 ERR ERR K28.5- K28.5+ D D
Lane2 K28.5- D21.5 K28.5+ D10.2 ERR ERR K28.5- K28.5+ K28.5- D21.5 K28.5+ D10.2 ERR ERR K28.5- K28.5+ K28.5- D21.5
Lane3 K28.5- D21.5 K28.5+ D10.2 ERR ERR K28.5- K28.5+ K28.5- D21.5 K28.5+ D10.2 ERR ERR K28.5- K28.5+ K28.5- D21.5
Lane4 K28.5- D21.5 K28.5+ D10.2 ERR ERR K28.5- K28.5+ K28.5- D21.5 K28.5+ D10.2 ERR ERR K28.5- K28.5+ K28.5- D21.5
Lane5 K28.5- D21.5 K28.5+ D10.2 ERR ERR K28.5- K28.5+ K28.5- D21.5 K28.5+ D10.2 ERR ERR K28.5- K28.5+ K28.5- D21.5
Lane6 K28.5- D21.5 K28.5+ D10.2 ERR ERR K28.5- K28.5+ K28.5- D21.5 K28.5+ D10.2 ERR ERR K28.5- K28.5+ K28.5- D21.5
Lane7 K28.5- D21.5 K28.5+ D10.2 ERR ERR K28.5- K28.5+ K28.5- D21.5 K28.5+ D10.2 ERR ERR K28.5- K28.5+ K28.5- D21.5
Lane8 D D D D K28.5- D21.5 K28.5+ D10.2 ERR ERR K28.5- K28.5+ K28.7- K28.7- K28.7- K28.7- K28.5- D21.5
Lane9 K28.5- D21.5 K28.5+ D10.2 ERR ERR K28.5- K28.5+ K28.5- D21.5 K28.5+ D10.2 ERR ERR K28.5- K28.5+ D D
Key:
K28.5- COM when disparity is negative, specifically: “0011111010”
K28.5+ COM when disparity is positive, specifically: “1100000101”
D21.5 Out of phase data Symbol specifically: “1010101010”
D10.2 Out of phase data Symbol, specifically: “0101010101”
D Delay Symbol K28.5 (with appropriate disparity)
ERR error status Symbol (with appropriate disparity)
K28.7- EIE when disparity is negative, specifically “0011111000”
20
The reason two identical error Symbols are inserted instead of one is to ensure disparity of the
8b/10b sequence is not impacted by the addition of the error status Symbol.
PCI Express Base Specification, Rev. 4.0 Version 1.0
371
All other Compliance pattern rules are identical (i.e., the rules for adding delay Symbols) so as to
preserve all the crosstalk characteristics of the Compliance Pattern.
The error status Symbol is an 8b/10b data Symbol, maintained on a per-Lane basis, and defined in
8-bit domain in the following way:
Receiver Error Count (Bits 6:0) - Incremented on every Receiver error after 5  the Pattern Lock bit
becomes asserted.
 Pattern Lock (Bit 7) - Asserted when the Lane locks to the incoming Modified Compliance
Pattern.
4.2.10 Compliance Pattern in 128b/130b Encoding
10 The compliance pattern consists of the following repeating sequence of 36 Blocks
1. One block with a Sync Header of 01b followed by a 128-bit unscrambled payload of 64 1’s
followed by 64 0’s
2. One block with a Sync Header of 01b followed by a 128-bit unscrambled payload of the
following:
Lane No
modulo
8 = 0
Lane No
modulo
8 = 1
Lane No
modulo
8 = 2
Lane No
modulo
8 = 3
Lane No
modulo
8 = 4
Lane No
modulo
8 = 5
Lane No
modulo
8 = 6
Lane No
modulo 8 =
7
Symbol 0 55h FFh FFh FFh 55h FFh FFh FFh
Symbol 1 55h FFh FFh FFh 55h FFh FFh FFh
Symbol 2 55h 00h FFh FFh 55h FFh FFh FFh
Symbol 3 55h 00h FFh FFh 55h FFh F0h F0h
Symbol 4 55h 00h FFh C0h 55h FFh 00h 00h
Symbol 5 55h 00h C0h 00h 55h E0h 00h 00h
Symbol 6 55h 00h 00h 00h 55h 00h 00h 00h
Symbol 7 {P,~P} {P,~P} {P,~P} {P,~P} {P,~P} {P,~P} {P,~P} {P,~P}
Symbol 8 00h 1Eh 2Dh 3Ch 4Bh 5Ah 69h 78h
Symbol 9 00h 55h 00h 00h 00h 55h 00h F0h
Symbol 10 00h 55h 00h 00h 00h 55h 00h 00h
Symbol 11 00h 55h 00h 00h 00h 55h 00h 00h
Symbol 12 00h 55h 0Fh 0Fh 00h 55h 07h 00h
Symbol 13 00h 55h FFh FFh 00h 55h FFh 00h
Symbol 14 00h 55h FFh FFh 7Fh 55h FFh 00h
Symbol 15 00h 55h FFh FFh FFh 55h FFh 00h
Key: P: Indicates the 4-bit encoding of the Transmitter preset value being used.
~P: Indicates the bit-wise inverse of P.
15
PCI Express Base Specification, Rev. 4.0 Version 1.0
372
3. One block with a Sync Header of 01b followed by a 128-bit unscrambled payload of the
following:
Lane No
modulo 8
= 0
Lane No
modulo 8
= 1
Lane No
modulo 8
= 2
Lane No
modulo 8
= 3
Lane No
modulo 8
= 4
Lane No
modulo 8
= 5
Lane No
modulo 8
= 6
Lane No
modulo 8
= 7
Symbol 0 FFh FFh 55h FFh FFh FFh 55h FFh
Symbol 1 FFh FFh 55h FFh FFh FFh 55h FFh
Symbol 2 FFh FFh 55h FFh FFh FFh 55h FFh
Symbol 3 F0h F0h 55h F0h F0h F0h 55h F0h
Symbol 4 00h 00h 55h 00h 00h 00h 55h 00h
Symbol 5 00h 00h 55h 00h 00h 00h 55h 00h
Symbol 6 00h 00h 55h 00h 00h 00h 55h 00h
Symbol 7 {P,~P} {P,~P} {P,~P} {P,~P} {P,~P} {P,~P} {P,~P} {P,~P}
Symbol 8 00h 1Eh 2Dh 3Ch 4Bh 5Ah 69h 78h
Symbol 9 00h 00h 00h 55h 00h 00h 00h 55h
Symbol 10 00h 00h 00h 55h 00h 00h 00h 55h
Symbol 11 00h 00h 00h 55h 00h 00h 00h 55h
Symbol 12 FFh 0Fh 0Fh 55h 0Fh 0Fh 0Fh 55h
Symbol 13 FFh FFh FFh 55h FFh FFh FFh 55h
Symbol 14 FFh FFh FFh 55h FFh FFh FFh 55h
Symbol 15 FFh FFh FFh 55h FFh FFh FFh 55h
Key: P: Indicates the 4-bit encoding of the Transmitter preset being used.
~P: Indicates the bit-wise inverse of P.
4. One EIEOS Block
5. 32 Data Blocks, each with a payload of 16 IDL data S 5 ymbols (00h) scrambled
IMPLEMENTATION NOTE
First Two Blocks of the Compliance Pattern
The first block is a very low frequency pattern to help with measurement of the preset settings. The
second block is to notify the Lane number and preset encoding the compliance pattern is using
10 along with ensuring the entire compliance pattern is DC Balanced.
The payload in each Data Block is the output of the scrambler in that Lane (i.e., input data is 0b).
The scrambler does not advance during the Sync Header bits. The scrambler is initialized when an
EIEOS is transmitted. The Lane numbers used to determine the scrambling LFSR seed value
depend on how Polling.Compliance is entered. If it is entered due to the Enter Compliance bit in
15 the Link Control 2 register being set, then the Lane numbers are the numbers that were assigned to
the Lanes and the Receiver Lane polarity to be used on each Lane is the Lane polarity inversion that
was used in the most recent time that LinkUp was 1b. If a Lane was not part of the configured Link
PCI Express Base Specification, Rev. 4.0 Version 1.0
373
at that time, and for all other methods of entering Polling.Compliance, the Lane numbers are the
default numbers assigned by the Port. These default numbers must be unique. For example, each
Lane of a x16 Link must be assigned a unique Lane number between 0 to 15. The Data Blocks of
the compliance pattern do not form a Data Stream and hence are exempt from the requirement of
transmitting an SDS Ordered Set or EDS Token during Ordered Set Block 5 to Data Block transition
and vice-versa.
IMPLEMENTATION NOTE
Ordered Sets in Compliance and Modified Compliance Patterns in
128b/130b Encoding
The various Ordered Sets (e.g., EIEOS and SKP OS) follow the Ordered Set definition
corresponding to the current Data Rate of operation. For example, at 16.0 GT/s Data Rate, the
EIEOS is the 16.0 GT/s EIEOS whereas at 8.0 GT/s Data Rate, the EIEOS is the 8.0 GT/s
10 EIEOS defined earlier. As defined in Section 4.2.7, the SKP Ordered Set is the Standard SKP
Ordered Set.
4.2.11 Modified Compliance Pattern in 128b/130b Encoding
The modified compliance pattern, when not operating in SRIS, consists of repeating the following
sequence of 65792 Blocks:
15 1. One EIEOS Block
2. 256 Data Blocks, each with a payload of 16 Idle data Symbols (00h), scrambled
3. 255 sets of the following sequence:
i. One SKP Ordered Set
ii. 256 Data Blocks, each with a payload of 16 Idle data Symbols (00h), scrambled
20 The modified compliance pattern, when operating in SRIS, consists of repeating the following
sequence of 67585 Blocks:
1. One EIEOS Block
2. 2048 sets of the following sequence:
i. One SKP Ordered Set
25 ii. 32 Data Blocks, each with a payload of 16 Idle data Symbols (00h), scrambled
The payload in each Data Block is the output of the scrambler in that Lane (i.e., input data is 0b).
The scrambler does not advance during the Sync Header bits. The scrambler is initialized when an
EIEOS is transmitted. The Lane numbers used to determine the scrambling LFSR seed value
depend on how Polling.Compliance is entered. If it is entered due to the Enter Compliance bit in
30 the Link Control 2 register being set, then the Lane numbers are the numbers that were assigned to
the Lanes and the Receiver Lane polarity to be used on each Lane is the Lane polarity inversion used
in the most recent time that LinkUp was 1b. If a Lane was not part of the configured Link at that
time, and for all other methods of entering Polling.Compliance, the Lane numbers are the default
numbers assigned by the Port. These default numbers must be unique. For example, each Lane of a
PCI Express Base Specification, Rev. 4.0 Version 1.0
374
x16 Link must be assigned a unique Lane number from 0 to 15. The Data Blocks of the modified
compliance pattern do not form a Data Stream and hence are exempt from the requirement of
transmitting an SDS Ordered Set or EDS Token during Ordered Set Block to Data Block transition
and vice-versa.
4.2.12 Jitter Measurement 5 Pattern in 128b/130b
The jitter measurement pattern consists of repeating the following Block:
 Sync Header of 01b followed by a 128-bit unscrambled payload of 16 Symbols of 55h
This generates a pattern of alternating 1s and 0s for measuring the transmitter’s jitter.
4.2.13 Lane Margining at Receiver
10 Lane Margining at Receiver, as defined in this Section, is mandatory for all Ports supporting 16.0
GT/s Data Rate, including Pseudo Ports (Retimers). Lane Margining at Receiver enables system
software to obtain the margin information of a given Receiver while the Link is in the L0 state. The
margin information includes both voltage and time, in either direction from the current Receiver
position. For all Ports that implement Lane Margining at Receiver, Lane Margining at Receiver for
15 timing is required, while support of Lane Margining at Receiver for voltage is optional.
Lane Margining at Receiver begins when a margin command is received, the Link is operating at
16.0 GT/s Data Rate or higher, and the Link is in L0 state. Lane Margining at Receiver ends when
either a ‘Go to Normal Settings’ command is received, the Link changes speed, or the Link exits
either the L0 or Recovery states. Lane Margining at Receiver optionally ends when certain error
20 thresholds are exceeded. Lane Margining at Receiver is is permitted to be suspended while the Link
is in Recovery for independent samplers.
Lane Margining at Receiver is not supported by PCIe Links operating at 2.5 GT/s, 5.0 GT/s, or 8.0
GT/s.
Software uses the per-Lane Margining Lane Control and Margining Lane Status registers in each
25 Port (Downstream or Upstream) for sending margin commands and obtaining margin status
information for the corresponding Receiver associated with the Port. For the Retimers, the
commands to get information about the Receiver’s capabilities and status and the commands to
margin the Receiver are conveyed in the Control SKP Ordered Sets in the Downstream direction.
The status and error reporting of the target Retimer Receiver is conveyed in the Control SKP
30 Ordered Sets in the Upstream direction. Software controls margining in the Receiver of a Retimer
by writing to the appropriate bits in the Margining Lane Control register in the Downstream Port.
The Downstream Port also updates the status information conveyed by the Retimer(s) in the Link
through the Control SKP Ordered Set into its Margining Lane Status register.
4.2.13.1 Receiver Number, Margin Type, Usage Model, and
35 Margin Payload Fields
The contents of the four command fields of the Margining Lane Control register in the
Downstream Port are always reflected in the identical fields in the Downstream Control SKP
Ordered Sets. The contents of the Upstream Control SKP Ordered Set received in the Downstream
PCI Express Base Specification, Rev. 4.0 Version 1.0
375
Port is always reflected in the corresponding status fields of the Margining Lane Status register in the
Downstream Port. The following table provides the bit placement of these fields in the Control SKP
Ordered Set.
Table 4-18: Margin Command Related Fields in the Control SKP Ordered Set
Symbol Description where the ‘Usage Model’ is ‘Lane Margining at Receiver’
4*N + 2 Bit 6: Usage Model
(0b: Lane Margining at Receiver, 1b: Reserved)
Bits [5:3]: Margin Type
Bits [2:0]: Receiver Number
4*N + 3 Bits [7:0]: Margin Payload
5
Usage Model: An encoding of 0b indicates that the usage model is Lane Margining at Receiver. An
encoding of 1b in this field is reserved for future usages.
If the ‘Usage Model’ field is 1b, Bits [5:0] of Symbol 4N+2 and Bits [7:0] of Symbol 4N+3 are
Reserved.
10 When evaluating received Control SKP Ordered Set for Margin Commands, all Receivers that do
not comprehend the usage associated with ‘Usage Model’ = 1b are required to ignore Bits[5:0] of
Symbol 4N+2 and Bits[7:0] of Symbol 4N+3 of the Control SKP Ordered Set, if the ‘Usage Model’
field is 1b.
15 IMPLEMENTATION NOTE
Potential future usage of Control SKP Ordered Set
The intended usage for the 15 bits of information in the Control SKP Ordered Set, as defined in
Table 4-18 is Lane Margining at Receiver. However a single bit (Bit 7 of Symbol 4N+2) is Reserved
for any future usage beyond Lane Margining at Receiver. If such a usage is defined in the future, this
20 bit will be set to 1b and the remaining 14 bits can be defined as needed by the new usage model.
Alternatively, Symbol 4N could use a different encoding than 78h for any future usage, permitting all
bits in Symbols 4N+1, 4N+2, and 4N+3 to be defined for that usage model.
Receiver Number:Receivers are identified in Figure 4-32. The following ‘Receiver Number’
25 encodings are used in the Downstream Port for Margin Commands targeting that Downstream Port
or a Retimer below that Downstream Port:
000b: Broadcast (Downstream Port Receiver and all Retimer Pseudo Port Receivers)
001b: Rx(A) (Downstream Port Receiver)
010b: Rx(B) (Retimer X or Z Upstream Pseudo Port Receiver)
30 011b: Rx(C) (Retimer X or Z Downstream Pseudo Port Receiver)
100b: Rx(D) (Retimer Y Upstream Pseudo Port Receiver)
101b: Rx(E) (Retimer Y Downstream Pseudo Port Receiver)
110b: Reserved
PCI Express Base Specification, Rev. 4.0 Version 1.0
376
111b: Reserved
The following ‘Receiver Number’ encodings are used in the Upstream Port for Margin Commands
targeting that Upstream Port:
000b: Broadcast (Upstream Port Receiver)
5 001b: Reserved
010b: Reserved
011b: Reserved
100b: Reserved
101b: Reserved
10 110b: Rx (F) (Upstream Port Receiver)
111b: Reserved
Figure 4-32: Receiver Number Assignment
Margin Type and Margin Payload: The ‘Margin Type’ field together with a valid ‘Receiver
15 Number’(s), associated with the ‘Margin Type’ encoding, and specific ‘Margin Payload’ field define
various commands used for margining (referred to as ‘margin command’). Table 4-19 defines the
encodings of valid margin commands along with the corresponding responses, used in both the
Control SKP Ordered Sets as well as the Margining Lane Control and Margining Lane Status
registers. Margin commands that are always broadcast will use the broadcast encoding for the
20 Receiver Number, even when only one Receiver is the target (e.g., USP or a DSP in a Link with no
Retimers). The Receiver Number field in the response to a margin command other than ‘No
Command’ reflects the number of the Receiver that is responding, even for a margin command that
is broadcast. The margin commands go Downstream whereas the responses go Upstream in the
PCI Express Base Specification, Rev. 4.0 Version 1.0
377
Control SKP Ordered Sets. The responses reflect the ‘Margin Type’ to which the target Receiver is
responding. The Receiver Number field of the response corresponds to the target Receiver that is
responding. The various parameters such as MSampleCount used here are defined in Section 8.4.4. All the
unused encodings described below are ‘Reserved’ and must not considered to be a valid margin
5 command.
Table 4-19: Margin Commands and Corresponding Responses
Command Response
Margin
Command
Margin
Type
[2:0]
Valid
Receiver
Number(s)
[2:0]
Margin
Payload
[7:0]
Margin
Type
[2:0]
Margin Payload [7:0]
No Command 111b 000b 9Ch
(‘No Command’ is also an independent command in
Upstream direction. The expected Response is ‘No
Command’ with the Receiver Number = 000b.)
Access Retimer
register
(Optional)
001b 010b, 100b Register
offset in
bytes:
00h – 87h,
A0h – FFh
001b Register value, if supported.
Target Receiver on Retimer
returns 00h if it does not
support accessing its registers.
Report Margin
Control
Capabilities
001b 001b
through
110b
88h 001b Margin Payload[7:5] =
Reserved;
Margin Payload[4:0] = {
MIndErrorSampler,
MSampleReportingMethod,
MIndLeftRightTiming, MIndUpDownVoltage,
MVoltageSupported }
Report
MNumVoltageSteps
001b 001b
through
110b
89h 001b Margin Payload [7] = Reserved
Margin Payload[6:0] =
MNumVoltageSteps
Report
MNumTimingSteps
001b 001b
through
110b
8Ah 001b Margin Payload [7:6] =
Reserved
Margin Payload [5:0] =
MNumTimingSteps
Report
MMaxTimingOffset
001b 001b
through
110b
8Bh 001b Margin Payload [7] = Reserved
Margin Payload[6:0] =
MMaxTimingOffset
Report
MMaxVoltageOffset
001b 001b
through
110b
8Ch 001b Margin Payload [7] = Reserved
Margin Payload[6:0] =
MMaxVoltageOffset
Report
MSamplingRateVoltage
001b 001b
through
110b
8Dh 001b Margin Payload [7:6] =
Reserved
Margin Payload[5:0] =
{ MSamplingRateVoltage [5:0]}
Report
MSamplingRateTiming
001b 001b
through
110b
8Eh 001b Margin Payload [7:6] =
Reserved
Margin Payload[5:0] =
{ MSamplingRateTiming [5:0]}
PCI Express Base Specification, Rev. 4.0 Version 1.0
378
Command Response
Margin
Command
Margin
Type
[2:0]
Valid
Receiver
Number(s)
[2:0]
Margin
Payload
[7:0]
Margin
Type
[2:0]
Margin Payload [7:0]
Report
MSampleCount
001b 001b
through
110b
8Fh 001b Margin Payload [7] = Reserved
Margin Payload[6:0] =
MSampleCount
Report MMaxLanes 001b 001b
through
110b
90h 001b Margin Payload [7:5] =
Reserved
Margin Payload[4:0] = MMaxLanes
Report
Reserved
001b 001b
through
110b
91-9Fh 001b Margin Payload[7:0] =
Reserved
Set Error Count
Limit
010b 001b
through
110b
Margin
Payload [7:6]
= 11b
Margin
Payload[5:0]
= Error
Count Limit
010b Margin Payload [7:6] = 11b
Margin Payload[5:0] = Error
Count Limit registered by the
target Receiver
Go to Normal
Settings
010b 000b
through
110b
0Fh 010b 0Fh
Clear Error Log 010b 000b
through
110b
55h 010b 55h
Step Margin to
timing offset to
right/left of
default
011b 001b
through
110b
See Section
4.2.13.1.2
011b Margin Payload[7:6] =
Step Margin Execution Status
(see Section 4.2.13.1.1)
Margin Payload[5:0] =
MErrorCount
Step Margin to
voltage offset to
up/down of
default
100b 001b
through
110b
See Section
4.2.13.1.2
100b Margin Payload[7:6] =
Step Margin Execution Status
(see Section 4.2.13.1.1)
Margin Payload[5:0] =
MErrorCount
Vendor Defined 101b 001b
through
110b
Vendor
Defined
101b Vendor Defined
4.2.13.1.1 Step Margin Execution Status
The Step Margin Execution Status used in Table 4-19 is a 2-bit field defined as follows:
 11b: NAK. Indicates that an unsupported Lane Margining command was issued. For
example,timing margin beyond +/- 0.2 UI. MErrorCount is 0.
PCI Express Base Specification, Rev. 4.0 Version 1.0
379
10b: Margining in progress. The Receiver is executing the step  margin command. MErrorCount
reflects the number of errors detected as defined in Section 8.4.4.
 01b: Set up for margin in progress. This indicates the Receiver is getting ready but has not yet
started executing the step margin command. MErrorCount is 0.
5  00b: Too many errors – Receiver autonomously went back to its default settings. MErrorCount
reflects the number of errors detected as defined in Section 8.4.4. Note that MErrorCount might be
greater than Error Count Limit.
4.2.13.1.2 Margin Payload for Step Margin Commands
For the ‘Step Margin to timing offset to right/left of default’ command, the Margin Payload field is
10 defined as follows:
 Margin Payload [7]: Reserved.
 If MIndLeftRightTiming for the targeted Receiver is Set:
o Margin Payload [6] indicates whether the margin command is right vs left. A 0b indicates
to move the Receiver to the right of the normal setting whereas a 1b indicates to move
15 the Receiver to the left of the normal setting.
o Margin Payload [5:0] indicates the number of steps to the left or right of the normal
setting.
 If MIndLeftRightTiming for the targeted Receiver is Clear:
o Margin Payload [6]: Reserved
20 o Margin Payload [5:0] indicates the number of steps beyond the normal setting.
For the ‘Step Margin to voltage offset to up/down of default’ command, the Margin Payload field is
defined as follows:
 If MIndUpDownVoltage for the targeted Receiver is Set:
o Margin Payload [7] indicates whether the margin command is up vs down. A 0b indicates
25 to move the Receiver up from the normal setting whereas a 1b indicates to move the
Receiver down from the normal setting.
o Margin Payload [6:0] indicates the number of steps up or down from the normal setting.
 If MIndUpDownVoltage for the targeted Receiver is Clear:
o Margin Payload [7]: Reserved
30 o Margin Payload [6:0] indicates the number of steps beyond the normal setting.
4.2.13.2 Margin Command and Response Flow
Each Receiver advertises its capabilities as defined in Section 8.4.4. The Receiver being margined
must report the number of errors that are consistent with data samples occurring at the indicated
location for margining. For simplicity, the margin commands and requirements are described in
35 terms of moving the data sampler location though the actual margining method may be
implementation specific. For example, the timing margin could be implemented on the actual data
PCI Express Base Specification, Rev. 4.0 Version 1.0
380
sampler or an independent/error sampler. Further, the timing margin can be implemented by
injecting an appropriate amount of stress/jitter to the data sample location, or by actually moving
the data/error sample location. When an independent data/error sampler is used, the errors
encountered with the independent data/error sampler must be reported in MErrorCount even though
the Link may not experience any errors. To margin a Receiver, Software moves 5 the target Receiver
to a voltage/timing offset from its default sampling position.
The following rules must be followed:
 Every Retimer Upstream Pseudo Port Receiver and the Downstream Port Receiver must
compute the ‘Margin CRC’ and ‘Margin Parity’ bits and compare against the received ‘Margin
10 CRC’ and ‘Margin Parity’ bits. Any mismatch must result in ignoring the contents of Symbols
4N+2 and 4N+3. A Downstream Port Receiver must report ‘Margin CRC’ and ‘Margin Parity’
errors in the Lane Error Status Register (see Section 7.7.3.3).
 The Upstream Port Receiver is permitted to ignore the ‘Margin CRC’ bits, ‘Margin Parity’ bits,
and all bits in the Symbols 4N+2 and 4N+3 of the Control SKP Ordered Set. If it checks
15 ‘Margin CRC’ and ‘Margin Parity’, any mismatch must be reported in the Lane Error Status
Register.
 The Downstream Port must transmit Control SKP Ordered Sets in each Lane, with the ‘Margin
Type’, ‘Receiver Number’, ‘Usage Model’, and ‘Margin Payload’ fields reflecting the
corresponding control fields in the Margining Lane Control register. Any Control SKP Ordered
20 Set transmitted more than 10 μsec after the Configuration Write Completion must reflect the
Margining Lane Control values written by that Configuration Write.
o This requirement applies regardless of the values in the Margining Lane Control register.
o This requirement applies regardless of the number of Retimer(s) in the Link.
 For Control SKP Ordered Sets received by the Upstream Pseudo Port, a Retimer Receiver is the
25 target of a valid margin command, if all of the following conditions are true:
o the ‘Margin Type’ is not ‘No Command’
o the ‘Receiver Number’ is the number assigned to the Receiver, or ‘Margin Type’ is either
‘Clear Error Log’ or ‘Go to Normal Settings’ and the ‘Receiver Number’ is ‘Broadcast’.
o the ‘Usage Model’ field is 0b
30 o the ‘Margin Type’, ‘Receiver Number’, and ‘Margin Payload’ fields are consistent with
the definitions in Table 4-18
o the CRC check and Margin Parity check pass.
 For Upstream and Downstream Ports, a Receiver is the target of a valid margin command, if all
of the following conditions are true for its Margining Lane Control register:
35 o the ‘Margin Type’ is not ‘No Command’
o the ‘Receiver Number’ is the number assigned to the Receiver or ‘Margin Type’ is either
‘Clear Error Log’ or ‘Go to Normal Settings’ and the ‘Receiver Number’ is ‘Broadcast’
o the ‘Usage Model’ field is 0b
o the ‘Margin Type’, the ‘Receiver Number’, and ‘Margin Payload’ fields are consistent
40 with the definitions in Table 4-19
PCI Express Base Specification, Rev. 4.0 Version 1.0
381
The Upstream Port must transmit the Control SKP Ordered  Set with ‘No Command’.
 A target Receiver must apply and respond to the margin command within 1ms of receiving the
valid margin command if the Link is still in L0 state and operating at 16.0 GT/s Data Rate.
o A target Receiver in a Retimer must send a response in the Control SKP Ordered Set in
5 the Upstream Direction within 1 ms of receiving the margin command.
o A target Receiver in the Upstream Port must update the Status field of the Lane Margin
Command and Status register within 1 ms of receiving the margin command.
o A target Receiver in the Downstream Port must update the Status field of the Lane
Margin Command and Status register within 1 ms of receiving the margin command if
10 the command is not broadcast or no Retimer(s) are present
 For a valid ‘Margin Type’, other than ‘No Command’, that is broadcast and received by a
Retimer:
o A Retimer, in position X (see Figure 4-32), forwards the response unmodified in the
Upstream Control SKP Ordered Set, if the command has been applied, else it sends the
15 ‘No Command’.
o The Receiver Number field of the response must be set to an encoding of one of the
Retimer's Pseudo Ports.
o The Retimer must respond only after both Pseudo Ports have completed the Margin
Command.
20  The Retimer must overwrite Bits [4:0] of Symbol 4N+1, Bits[7, 5:0] of Symbol 4N+2 and Bits
[7:0] in Symbol 4N+3 as it forwards the Control SKP Ordered Set in the Upstream direction if it
is the target Receiver of a margin command and is executing the command.
 On receipt of a Control SKP Ordered Set, the Downstream Port must reflect the Margining
Lane Status register from the corresponding fields in the received Control SKP Ordered Set
25 within 1 μsec, if it passes the ‘Margin CRC’ and ‘Margin Parity’ checks and one of the following
conditions apply:
o In the Margining Lane Control register: ‘Receiver Number’ is 010b through 101b
o In the Margining Lane Control register: ‘Receiver Number’ is 000b, ‘Margin Command’
is ‘Clear Error Log’, ‘No Command’, or ‘Go to Normal Settings’, and there are
30 Retimer(s) in the Link
o Optionally, if the Margining Lane Control register 'Usage Model' field is 1b
o Optionally, if the Margining Lane Control register 'Receiver Number' field is 110b or
111b
The Margining Lane Status register fields are updated regardless of the Usage Model bit in the
35 received Control SKP Ordered Set.
 A component must advertise the same value for each parameter defined in Table 8-12 in Section
8.4.4 across all its Receivers. A component must not change any parameter value except for
MSampleCount and MErrorCount defined in Table 8-12 in Section 8.4.4 while LinkUp = 1b.
 A target Receiver that receives a valid ‘Step Margin’ command must continue to apply that offset
40 until any of the following occur:
PCI Express Base Specification, Rev. 4.0 Version 1.0
382
o it receives a valid ‘Go to Normal Settings’ command
o it receives a subsequent valid ‘Step Margin’ command with different ‘Margin Type’ or
‘Margin Payload’ field
o MIndErrorSampler is 0b and MErrorCount exceeds ‘Error Count Limit’
o Optionally, MIndErrorSampler is 1b and MErrorCount exceeds 5 ‘Error Count Limit’.
 If a ‘Step Margin’ command terminates because MErrorCount exceeds ‘Error Count Limit’, the target
Receiver must automatically return to its default sample position and indicate this in the ‘Margin
Payload’ field (‘Step Margin Execution Status’ = 00b). Note: termination for this reason is
optional if MIndErrorSampler is 1b.
10  If MIndErrorSampler is 0b, an error is detected when:
o The target Receiver is a Port that enters Recovery or detects a Data Parity mismatch
while in L0
o The target Receiver is a Pseudo Port that enters Forwarding training sets or detects a
Data Parity mismatch while forwarding non-training sets.
15  If MIndErrorSampler is 1b, an error is detected when:
o The target Receiver is a Port and a bit error is detected while in L0
o The target Receiver is a Pseudo Port and a bit error is detected while the Retimer is
forwarding non-training sets
 If MIndErrorSampler is 0b and either (1) the target Receiver is a Port that enters Recovery or (2) the
20 target Receiver is a Pseudo Port that enters Forwarding training sets:
o The target Receiver must go back to the default sample position
o If the target Receiver is a Port that is still performing margining, it must resume the
margin position within 128 μsec of entering L0
o If the target Receiver is a Pseudo Port that is still performing margining, it must resume
25 the margin position within 128 μsec of Forwarding non-training sets
 A target Receiver is required to clear its accumulated error count on receiving ‘Clear Error Log’
command, while it continues to margin (if it is the target Receiver of a ‘Step Margin’ command
still in progress), if it was doing so.
 For a target Receiver of a ‘Set Error Count Limit’ command, the new value is used for all future
30 ‘Step Margin’ commands until a new ’Set Error Count Limit’ command is received.
 If no ‘Set Error Count Limit’ is received by a Receiver since entering L0, the default value is 4.
 Behavior is undefined if a ‘Set Error Count Limit’ command is received while a ‘Step Margin’
command is in effect.
 Once a target Receiver reports a ‘Step Margin Execution Status’ of 11b (NAK) or 00b (‘Too
35 many errors’), it must continue to report the same status as long as the ‘Step Margin’ command
is in effect.
 A target Receiver must not report a ‘Step Margin Execution Status’ of 01b (‘Set up for margin in
progress’) for more than 100 ms after it receives a new valid ‘Step Margin’ command
PCI Express Base Specification, Rev. 4.0 Version 1.0
383
A target Receiver that reports a ‘Step Margin Execution Status’ other  than 01b, cannot report
01b subsequently unless it receives a new valid ‘Step Margin’ command.
 Reserved bits in the Margin Payload must follow these rules:
o The Downstream or Upstream Port must transmit 0s for Reserved bits
5 o The retimer must forward Reserved bits unmodified
o All Receivers must ignore Reserved bits
 Reserved encodings of the ‘Margin Command’, ‘Receiver Number’, or ‘Margin Payload’ fields
must follow these rules:
o The retimer must forward Reserved encodings unmodified
10 o All Receivers must treat Reserved encodings as if they are not the target of the margin
command
 A Vendor Defined margin command or response, that is not defined by a retimer is ignored and
forwarded normally.
 A target Receiver on a Retimer must return 00h on the response payload on ‘Access Retimer
15 register’ command, if it does not support register access. If a Retimer supports ‘Access Retimer
register’ command, the following must be observed:
o It must return a non-zero value for the DWORD at locations 80h and 84h respectively.
o It must not place any registers corresponding to ‘Margin Payload’ locations 88h through
9Fh.
20 4.2.13.3 Receiver Margin Testing Requirements
Software must ensure that the following conditions are met before performing Lane Margining at
Receiver:
 The current Link data rate must be 16.0 GT/s.
 The current Link width must include the Lanes that are to be tested.
25  The Upstream Port’s Function(s) must be programmed to a D-state that prevents the Port from
entering the L1 Link state. See Section 5.2 for more information.
 The ASPM Control field of the Link Control register must be set to 00b (Disabled) in both the
Downstream Port and Upstream Port.
 The Hardware Autonomous Speed Disable bit of the Link Control 2 register must be set to 1b
30 in both the Downstream Port and Upstream Port.
 The Hardware Autonomous Width Disable bit of the Link Control register must be set to 1b in
both the Downstream Port and Upstream Port.
While margining, software must ensure the following:
 All margin commands must have the ‘Usage Model’ field in the Margining Lane Control register
35 set to 0b. While checking for the status of an outstanding margin command, software must
check that the ‘Usage Model’ field of the status part of the Margining Lane Status register is set
to 0b.
