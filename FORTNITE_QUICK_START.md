# City of Legends - Quick Setup Guide

## 🚀 Get Started in 30 Minutes

This guide will help you create a basic functioning roleplay map in Fortnite Creative. Follow these steps to build your city!

---

## ⚙️ Prerequisites

### What You Need
- ✅ Fortnite installed (any platform: PC, Console, Mobile)
- ✅ Epic Games account
- ✅ Access to Creative Mode
- ✅ 2-4 hours of building time for basic setup
- ✅ Patience and creativity!

---

## 📋 Phase 1: Basic Map Structure (30 minutes)

### Step 1: Create Your Island
1. Launch Fortnite
2. Navigate to **Creative Mode**
3. Select **Create** → **New Island**
4. Choose **Blank Island** template
5. Enter your new island

### Step 2: Set Up Grid
1. Open Phone Tool (Tab key on PC, Touchpad on PlayStation, View button on Xbox)
2. Enable **Grid Snap** for precise building
3. Set **Grid Size** to 1 unit for detailed work
4. Enable **Fly Mode** for easy navigation

### Step 3: Plan Your Districts
**Mark out these 6 areas on your island:**
1. **Downtown** (Center) - 8x8 grid squares
2. **Industrial Zone** (Northeast) - 6x6 grid squares
3. **Residential** (Southeast & Southwest) - 10x10 combined
4. **Entertainment** (West) - 4x4 grid squares
5. **Emergency Services** (North-Center) - 3x3 grid squares
6. **Outskirts** (Outer edges) - Remaining space

**Use colored props to mark boundaries temporarily!**

---

## 🏗️ Phase 2: Build Core Structures (2 hours)

### Essential Buildings (Priority Order)

#### 1. Police Station (30 min)
**Location**: Emergency Services Hub
**Required Elements**:
- Main building (use Downtown Gallery buildings)
- Vehicle garage (3 spawn points)
- Jail cells (3 rooms with barriers)
- Armory room (weapon storage)
- Front desk area

**Devices Needed**:
- 3x Spawner Device (police vehicles)
- 3x Barrier Device (jail cells)
- 1x Item Granter (police equipment)
- 1x Team Spawner (police spawn point)
- 2x Button Device (job join, vehicle request)

#### 2. Hospital (30 min)
**Location**: Emergency Services Hub
**Required Elements**:
- Emergency entrance bay
- Patient rooms (4-6 rooms)
- Operating room
- Parking for ambulances (2 spawn points)
- Medical supply room

**Devices Needed**:
- 2x Spawner Device (ambulances)
- 1x Item Granter (medical supplies)
- 1x Team Spawner (EMS spawn point)
- 1x Button Device (job join)

#### 3. Fire Station (20 min)
**Location**: Emergency Services Hub
**Required Elements**:
- Fire truck garage (2 spawn points)
- Equipment room
- Living quarters
- Dispatch area

**Devices Needed**:
- 2x Spawner Device (fire trucks)
- 1x Item Granter (firefighter gear)
- 1x Team Spawner (firefighter spawn point)
- 1x Button Device (job join)

#### 4. City Hall / Employment Center (20 min)
**Location**: Downtown
**Required Elements**:
- Large lobby with job boards
- 10 job selection stations
- Mayor's office
- Information desk

**Devices Needed**:
- 10x Button Device (job selection: Police, EMS, Fire, Taxi, Retail, etc.)
- 1x HUD Message Device (welcome message)
- 1x Spawner (tutorial materials)

#### 5. Bank (20 min)
**Location**: Downtown
**Required Elements**:
- Customer service area
- ATM machines (4 locations)
- Vault (for heist events)
- Office spaces

**Devices Needed**:
- 4x Button Device (ATM interactions)
- 1x HUD Message Device (balance display)
- 2x Barrier Device (vault door)
- 1x Trigger Device (vault alarm)

#### 6. Car Dealership (15 min)
**Location**: Downtown or main road
**Required Elements**:
- Showroom floor
- Parking lot (vehicle displays)
- Sales office
- Service bay

**Devices Needed**:
- 1x Vending Machine (vehicle purchase)
- 5x Spawner Device (vehicle types)
- 5x Button Device (test drive / spawn vehicle)

#### 7. Sample Properties (15 min)
**Create 3-4 example properties:**
- 1x Small apartment
- 1x Medium house
- 1x Luxury penthouse
- 1x Commercial storefront

**Devices Needed (per property)**:
- 1x Conditional Button (purchase button)
- 1x Item Granter (property key)
- 1x Barrier Device (locked door)
- 1x Trigger Device (key detection)

---

## 🔧 Phase 3: Essential Device Setup (1 hour)

### Job System Configuration

#### Create Teams (10 min)
1. Open Phone → **Devices** → **Team Settings & Spawner**
2. Create these teams:
   - **Team 1**: Police (Blue color)
   - **Team 2**: EMS (Red color)
   - **Team 3**: Fire (Yellow color)
   - **Team 4-10**: Civilians (Green, Purple, etc.)
3. Set team spawn locations at their respective buildings

#### Job Selection Buttons (15 min)
**At City Hall/Employment Center:**

For each job, place a **Button Device**:

1. **Police Button Setup**:
   ```
   Button Text: "Join Police Force"
   Interaction Text: "Press E to become an Officer"
   
   Channel 1 → Team Settings: Change to Police Team
   Channel 2 → Item Granter: Grant Pistol, Handcuffs
   Channel 3 → HUD Message: "You are now a Police Officer"
   Channel 4 → Respawn: Send to Police Station
   ```

2. **EMS Button Setup**:
   ```
   Button Text: "Join EMS"
   Interaction Text: "Press E to become a Paramedic"
   
   Channel 5 → Team Settings: Change to EMS Team
   Channel 6 → Item Granter: Grant Medical Supplies
   Channel 7 → HUD Message: "You are now a Paramedic"
   Channel 8 → Respawn: Send to Hospital
   ```

3. **Fire Button Setup**:
   ```
   Button Text: "Join Fire Department"
   Interaction Text: "Press E to become a Firefighter"
   
   Channel 9 → Team Settings: Change to Fire Team
   Channel 10 → Item Granter: Grant Firefighter Tools
   Channel 11 → HUD Message: "You are now a Firefighter"
   Channel 12 → Respawn: Send to Fire Station
   ```

4. **Repeat for other jobs**: Taxi, Retail, Business, etc.

### Economy System Setup (20 min)

#### Configure Salary Payments
1. **Create Timer Device** (for each job area):
   ```
   Timer Duration: 600 seconds (10 minutes)
   Loop: Enabled
   Auto-Start: Enabled
   ```

2. **Place Trigger Device** at work areas:
   ```
   Trigger Size: Cover entire work area
   Team Filter: Set to specific job team
   Trigger When: Player enters and stays
   ```

3. **Add Accolade Device** (salary granter):
   ```
   Accolade Value: 100-200 gold bars (based on job)
   Grant When: Timer ends AND player in trigger
   ```

4. **Connect Devices**:
   ```
   Timer (Channel 20) → Trigger (Channel 21) → Accolade (Channel 22)
   Accolade (Channel 23) → HUD Message: "Salary Paid: $150"
   ```

#### Set Up Starting Money (5 min)
1. Place **Accolade Device** at spawn
2. Set to grant 2,000 gold bars
3. Set to activate "On Player Spawn"
4. Add HUD Message: "Welcome! Starting Balance: $2,000"

#### Configure ATMs (10 min)
1. Place **Button Device** at 4 ATM locations
2. Configure button:
   ```
   Button Text: "ATM - Check Balance"
   
   Channel 50 → HUD Message: Display gold bar count
   ```
3. Optional: Add Conditional Buttons for deposit/withdrawal

### Vehicle System Setup (15 min)

#### Car Dealership
1. **Place Vending Machine**:
   ```
   Items for Sale:
   - Off-Road Vehicle: 2,000 gold bars
   - Sports Car: 15,000 gold bars
   - Pickup Truck: 8,000 gold bars
   ```

2. **Place Spawner Devices** (one per vehicle type):
   ```
   Spawn Item: [Vehicle Type]
   Spawn Delay: 5 seconds
   Respawn Time: 60 seconds
   ```

3. **Connect Vending Machine** → **Spawner**:
   ```
   On Purchase → Activate Spawner (Channel 60-65)
   ```

#### Job Vehicle Spawners
1. **Police Vehicles** (at Police Station):
   - Place 3x Spawner Devices (patrol car, motorcycle, SUV)
   - Add Button: "Request Vehicle" (police team only)
   - Connect Button → Spawner

2. **EMS Vehicles** (at Hospital):
   - Place 2x Spawner Devices (ambulances)
   - Add Button: "Request Ambulance"
   - Connect Button → Spawner

3. **Fire Vehicles** (at Fire Station):
   - Place 2x Spawner Devices (fire trucks)
   - Add Button: "Request Fire Truck"
   - Connect Button → Spawner

---

## 🚨 Phase 4: Law Enforcement System (30 min)

### Arrest System Setup

#### Arrest Button (10 min)
1. Place **Conditional Button** (portable device police can use)
2. Configure:
   ```
   Button Text: "Arrest Suspect"
   Condition: Player must be on Police Team
   Interaction Range: 5 meters
   
   Channel 70 → Teleport Device: Send target to jail
   Channel 71 → Item Remover: Remove target's weapons
   Channel 72 → Barrier Device: Lock jail cell
   Channel 73 → Timer: Start jail time
   ```

#### Jail Cells (10 min)
1. Build 3 jail cells with **Barrier Devices** as doors
2. Place **Teleport Device** inside each cell
3. Configure Barrier:
   ```
   Initial State: Disabled (open)
   Activation: Close when prisoner teleported
   ```
4. Add **Timer Device**:
   ```
   Duration: 300-1800 seconds (5-30 minutes based on crime)
   On End: Open barrier (release prisoner)
   ```

#### Wanted Level System (10 min)
1. Place **Tracker Device** (tracks wanted stars):
   ```
   Tracker Name: "Wanted Level"
   Min Value: 0
   Max Value: 5
   Display: On HUD
   ```

2. Add triggers for crimes:
   - Player damages player: +1 wanted star
   - Player enters restricted area: +1 wanted star
   - Player activates bank alarm: +3 wanted stars

3. Display wanted stars with **HUD Message Device**

---

## 🎮 Phase 5: Testing & Polish (30 min)

### Solo Testing (15 min)
1. **Start Game** and test as player:
   - Join a job (try Police)
   - Receive equipment
   - Test vehicle spawning
   - Check salary payment (wait 10 min or speed up timer)
   - Test property purchase
   - Try arrest system

2. **Check Device Memory**:
   - Open Phone → Settings → Memory Usage
   - Should be below 80,000 / 100,000
   - If over: Remove decorative props, consolidate devices

3. **Fix Obvious Bugs**:
   - Devices not triggering? Check channels
   - Players stuck? Add collision
   - Vehicles not spawning? Check spawner settings

### Multiplayer Testing (15 min)
1. Invite 3-5 friends
2. Test:
   - Job selection (everyone picks different job)
   - Economy (check if salaries work for all players)
   - Vehicle spawning (test with multiple players)
   - Property purchase (test ownership conflicts)
   - Police arrest (test on volunteer)

3. Get feedback on:
   - Fun factor
   - Confusing mechanics
   - Balance issues
   - Performance problems

---

## 📢 Phase 6: Publishing (15 min)

### Prepare for Launch
1. **Set Island Name**: "City of Legends RP"
2. **Write Description**:
   ```
   🌆 City of Legends - Fortnite Roleplay
   
   32+ player roleplay server with jobs, economy, and properties!
   
   ✨ Features:
   - 10+ Jobs (Police, EMS, Fire, Taxi, Business, etc.)
   - Buy vehicles & properties
   - Active law enforcement
   - Player-driven economy
   
   📋 Rules: Stay in character, respect players, follow laws!
   ```

3. **Set Game Settings**:
   - Max Players: 40
   - Respawn: Enabled
   - Friendly Fire: Disabled (for safe zones)
   - Time Limit: None
   - Storm: Disabled

4. **Create Thumbnail**: Take screenshot of downtown area

### Publish Island
1. Open Phone Tool (Tab/Touchpad/View button)
2. Navigate to **My Island** tab
3. Click **Island Settings** button
4. Click **Publish** button at bottom
5. Select privacy setting: **Public** (or Private for testing)
6. Confirm publication
7. **Copy Island Code**: After publishing, click "Copy Code" button
8. Share code with players (format: XXXX-XXXX-XXXX)

### Share Your Map
- Post on r/FortniteCreative
- Share on Discord servers
- Tweet with #FortniteCreative #Roleplay
- Create YouTube trailer

---

## 🎯 Quick Reference Checklist

### Core Buildings
- [ ] Police Station (with jail cells)
- [ ] Hospital (with ambulances)
- [ ] Fire Station (with fire trucks)
- [ ] City Hall / Employment Center
- [ ] Bank (with ATMs)
- [ ] Car Dealership
- [ ] 3-4 Sample Properties

### Essential Devices
- [ ] 10+ Job selection buttons
- [ ] Team Settings (Police, EMS, Fire, Civilian teams)
- [ ] Salary payment system (Timer + Trigger + Accolade)
- [ ] Vehicle spawners (personal & job vehicles)
- [ ] Property purchase system (Conditional Button + Key)
- [ ] Arrest system (Conditional Button + Jail + Timer)
- [ ] Economy system (Vending Machines, ATMs)

### Testing Complete
- [ ] All jobs work correctly
- [ ] Salaries paid every 10 minutes
- [ ] Vehicles spawn properly
- [ ] Properties can be purchased
- [ ] Arrests send players to jail
- [ ] No critical bugs
- [ ] Performance is acceptable

### Published
- [ ] Island named and described
- [ ] Max players set to 40
- [ ] Game settings configured
- [ ] Island published publicly
- [ ] Island code shared

---

## 💡 Pro Tips

### Time-Saving Tricks
1. **Copy-Paste Buildings**: Build one property, copy it multiple times
2. **Use Prefabs**: Save common device setups as prefabs
3. **Device Templates**: Copy entire device chains for similar jobs
4. **Grid Snap**: Always use grid snap for clean alignment
5. **Test Early**: Test each system as you build it

### Common Mistakes to Avoid
1. ❌ Don't place all devices at once (test incrementally)
2. ❌ Don't forget to connect devices via channels
3. ❌ Don't overcomplicate (start simple, add complexity later)
4. ❌ Don't ignore memory limit (monitor constantly)
5. ❌ Don't skip testing (bugs multiply quickly)

### Next Steps After Basic Setup
1. Add more properties (expand to 20-30 buyable locations)
2. Create more jobs (mechanic, chef, business owner, etc.)
3. Add mini-games (racing, casino, heists)
4. Implement criminal activities (organized heists)
5. Create events (car meets, festivals, court trials)
6. Build more districts (airport, beach, industrial park)

---

## 🆘 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| Device not working | Check channel connections and team filters |
| Players stuck in walls | Add collision barriers, provide respawn button |
| Salaries not paying | Verify Timer → Trigger → Accolade connections |
| Vehicles not spawning | Check spawner settings and clear spawn area |
| Jail doors won't close | Check Barrier Device and teleport device channels |
| Memory limit exceeded | Remove decorative props, consolidate devices |
| Performance lag | Reduce active devices, simplify complex areas |

---

## 📚 Additional Resources

### Helpful Links
- **Fortnite Creative Official Docs**: Learn device basics
- **YouTube**: Search "Fortnite Creative Roleplay Tutorial"
- **Reddit**: r/FortniteCreative for tips and inspiration
- **Discord**: Join Fortnite Creative communities

### Recommended Videos
1. "Fortnite Creative Device Tutorial" - Learn all devices
2. "How to Make a Roleplay Map" - Full walkthrough
3. "Fortnite Creative Economy System" - Advanced money systems
4. "Police System Tutorial" - Arrest mechanics

---

<div align="center">

## 🎉 Congratulations!

You've created your first Fortnite Roleplay server!

**Now invite friends and start creating stories!**

*Remember: The best roleplay comes from player creativity, not just complex systems.*

---

**City of Legends - Quick Setup Guide**  
Version 1.0 | December 2025

</div>
