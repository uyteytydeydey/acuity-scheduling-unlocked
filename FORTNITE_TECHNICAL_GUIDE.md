# New Live - Technical Implementation Guide

## 📋 Table of Contents
1. [Fortnite Creative Basics](#fortnite-creative-basics)
2. [Device Setup](#device-setup)
3. [Economy System](#economy-system)
4. [Job System Implementation](#job-system-implementation)
5. [Property System](#property-system)
6. [Vehicle System](#vehicle-system)
7. [Law Enforcement Mechanics](#law-enforcement-mechanics)
8. [Phone System Implementation](#phone-system-implementation)
9. [Performance Optimization](#performance-optimization)
10. [Testing & Quality Assurance](#testing--quality-assurance)

---

## 🎮 Fortnite Creative Basics

### Creative Mode Limitations
- **Max Players**: 40 players per island
- **Device Memory**: 100,000 memory budget (monitor closely)
- **Island Size**: Maximum grid size of 25 x 25 terrain pieces
- **Prop Limit**: ~15,000 props (varies by complexity)
- **Device Channels**: 200 channels for device communication
- **Active Devices**: Monitor performance with complex device setups

### Essential Creative Tools
1. **Phone Tool**: Primary building and editing interface
2. **Grid Snap**: Align buildings and props perfectly
3. **Copy/Paste**: Duplicate complex structures
4. **Undo/Redo**: Fix mistakes quickly
5. **Fly Mode**: Navigate while building
6. **Device Gallery**: Access all interactive devices

### Recommended Creative Galleries
- **Downtown Galleries**: Modern city buildings
- **Suburbia Galleries**: Residential houses
- **Industrial Galleries**: Warehouses and factories
- **Vehicle Galleries**: Cars, trucks, emergency vehicles
- **Props Galleries**: Furniture, decorations, interactive objects
- **Device Galleries**: All functional game logic devices

---

## 🔧 Device Setup

### Core Devices Required

#### 1. **Spawner Device**
**Purpose**: Spawn vehicles, items, and equipment
**Configuration**:
- Set spawn location and rotation
- Configure spawn delay and quantity
- Set respawn time for vehicles
- Link to trigger devices for job-specific spawns

**Usage Examples**:
- Police vehicle spawners at station
- Medical equipment at hospital
- Tool spawners at workshops

#### 2. **Item Granter Device**
**Purpose**: Give players job equipment and tools
**Configuration**:
- Add items to grant list
- Set quantity for each item
- Link to team-based triggers
- Configure grant timing (on spawn, on button press)

**Usage Examples**:
- Grant police weapons when joining police team
- Give medical supplies to paramedics
- Provide tools to mechanics

#### 3. **HUD Message Device**
**Purpose**: Display notifications, job info, and system messages
**Configuration**:
- Set message text and duration
- Configure message color and position
- Set display conditions
- Link to trigger events

**Usage Examples**:
- Job salary payment notifications
- Emergency call alerts
- System announcements

#### 4. **Button Device**
**Purpose**: Interactive buttons for player actions
**Configuration**:
- Set button text and appearance
- Configure interaction type (hold/press)
- Set cooldown time
- Link to other devices via channels

**Usage Examples**:
- Clock in/out of work
- Open property doors
- Access vehicle spawners
- Trigger job actions

#### 5. **Conditional Button Device**
**Purpose**: Buttons with conditions (requires specific items, team, etc.)
**Configuration**:
- Set conditions (team, item possession, score)
- Configure button behavior
- Set success and failure actions
- Link to other devices

**Usage Examples**:
- Property access (requires ownership key)
- Job-specific actions (requires team membership)
- Purchase transactions (requires sufficient funds)

#### 6. **Trigger Device**
**Purpose**: Detect when players enter/exit areas
**Configuration**:
- Set trigger volume size
- Configure team/class filters
- Set trigger behavior (on enter, on exit, while inside)
- Link to other devices via channels

**Usage Examples**:
- Detect when player enters work zone (start pay timer)
- Detect bank entry (alert police if wanted)
- Detect property boundaries

#### 7. **Timer Device**
**Purpose**: Create time-based events
**Configuration**:
- Set countdown duration
- Configure loop behavior
- Set start/stop conditions
- Link to other devices

**Usage Examples**:
- Job salary payment timer (every 10 minutes)
- Police patrol check-ins
- Property tax collection timer

#### 8. **Team Settings & Spawner Device**
**Purpose**: Manage player teams for jobs
**Configuration**:
- Create teams for each job type
- Set team colors and names
- Configure spawn locations per team
- Set team-specific settings

**Teams Setup**:
1. Police Team (Blue)
2. EMS Team (Red)
3. Fire Team (Yellow)
4. Civilian Teams (Green, Purple, etc.)

#### 9. **Vending Machine Device**
**Purpose**: Purchase vehicles, properties, and items
**Configuration**:
- Set purchase price in gold bars
- Add items for sale
- Configure stock limits
- Set appearance and location

**Usage Examples**:
- Vehicle dealership (buy cars)
- Property office (buy homes/businesses)
- Weapon shop (legal firearms)
- Clothing store (cosmetics if applicable)

#### 10. **Mutator Zone Device**
**Purpose**: Create special zones with modified rules
**Configuration**:
- Set zone boundaries
- Configure gravity, speed, damage settings
- Set team/class permissions
- Link to other devices

**Usage Examples**:
- No-weapon zones (safe areas)
- Speed zones (highway fast travel)
- Private property zones

---

## 💰 Economy System

### Currency Implementation

#### Using Gold Bars as "New Coins"
Fortnite Creative uses **Gold Bars** as the primary currency system.

**Setup**:
1. **Accolade Device**: Grant gold bars as rewards
2. **Tracker Device**: Monitor player gold bar balance
3. **HUD Message**: Display balance to players
4. **Vending Machines**: Deduct gold bars for purchases

**Configuration**:
```
Accolade Device Settings:
- Accolade Value: 100-500 gold bars (salary amount)
- Trigger: Connect to Timer Device (every 10 minutes)
- Filter: By team (only grant to players on job teams)
```

### Salary Payment System

#### Automated Salary Payments
**Devices Required**:
- Timer Device (10-minute loop)
- Trigger Device (detect players in work zones)
- Accolade Device (grant gold bars)
- HUD Message Device (payment confirmation)

**Implementation Steps**:
1. Place **Trigger Device** in each job work area
2. Set Timer Device to 10-minute countdown (repeating)
3. Connect Timer → Trigger → Accolade (when timer ends, grant gold to players in trigger)
4. Connect Accolade → HUD Message (show "Salary Paid: $150 LC")

**Salary Amounts (Gold Bars)**:
- Police Officer: 200 bars/10 min
- Paramedic: 150 bars/10 min
- Firefighter: 150 bars/10 min
- Business Jobs: 150 bars/10 min
- Retail/Service: 100 bars/10 min
- Taxi/Delivery: 100 bars/10 min + tips

### Purchase System

#### Vehicle Purchase
**Devices Required**:
- Vending Machine Device (vehicle sales)
- Spawner Device (spawn purchased vehicle)
- Button Device (access purchased vehicle)

**Implementation**:
1. Place Vending Machine at car dealership
2. Add vehicles to vending machine with prices
3. Link Vending Machine → Spawner (spawn vehicle after purchase)
4. Optional: Use Class Designer to track ownership

#### Property Purchase
**Devices Required**:
- Conditional Button Device (purchase button)
- Item Granter (property key/card)
- Barrier Device (door access)
- HUD Message (confirmation)

**Implementation**:
1. Place Conditional Button at property entrance
2. Set condition: Requires gold bar amount
3. On successful purchase:
   - Grant property key/access card
   - Send HUD message confirming purchase
   - Update property ownership (track via item possession)
4. Link Conditional Button → Barrier (unlock door with key item)

### Banking System

#### ATM Machines
**Devices Required**:
- Button Device (ATM interface)
- HUD Message Device (balance display)
- Conditional Button Device (withdrawal/deposit)

**Implementation**:
1. Place Button Device at ATM locations (bank, gas stations)
2. On button press → Display HUD message with balance
3. Use Conditional Buttons for transactions
4. Track balance using gold bar system

---

## 👮 Job System Implementation

### Job Assignment System

#### Employment Center Setup
**Location**: City Hall or dedicated building
**Devices Required**:
- Multiple Button Devices (one per job)
- Team Settings Device
- Item Granter Device (job equipment)
- HUD Message Device (job instructions)

**Implementation**:
1. Create button for each job: "Join Police Force", "Become Paramedic", etc.
2. Connect each button to Team Settings:
   - Button Press → Change Player Team (to specific job team)
   - Button Press → Grant Job Equipment (weapons, tools, uniform)
   - Button Press → Display Job Instructions (HUD message)
   - Button Press → Teleport to Job HQ (optional)

**Example: Police Job Assignment**
```
Button: "Join Police Force"
↓
Team Settings: Set Player to Police Team (Blue)
↓
Item Granter: Grant Pistol, Handcuffs, Police Badge
↓
HUD Message: "Welcome Officer! Report to station for duty."
↓
Respawn Device: Spawn at Police Station
```

### Job-Specific Spawn Points

#### Setting Up Job HQs
**Devices Required**:
- Team Spawner Device (per job)
- Item Granter Device (spawn with equipment)
- Trigger Device (detect when player leaves spawn)

**Implementation**:
1. Place Team Spawner at job headquarters
2. Configure to only spawn specific team
3. Connect to Item Granter (give equipment on spawn)
4. Set spawn pad appearance (colored platform)

**Spawn Locations**:
- Police: Police Station main entrance
- EMS: Hospital emergency bay
- Fire: Fire Station garage
- Civilians: Multiple spawn points across residential areas
- Business: Downtown office district

### Work Zone Detection

#### Tracking Active Workers
**Devices Required**:
- Trigger Device (work area boundary)
- Timer Device (salary payment)
- Tracker Device (time worked)
- HUD Message Device (status updates)

**Implementation**:
1. Place large Trigger Device covering work area
2. Set filter: Only trigger for specific team
3. Connect Trigger → Timer (start salary timer when player enters)
4. Connect Timer → Accolade (grant salary every 10 minutes in zone)
5. Optional: Track time worked with Tracker Device

**Work Zones**:
- Police: Patrol routes and station
- EMS: Hospital and response areas
- Fire: Fire station and emergency zones
- Retail: Inside store/shop buildings
- Taxi: Anywhere in city (always working when in vehicle)

---

## 🏠 Property System

### Property Ownership

#### Implementing Ownership
**Method 1: Item-Based Ownership**
**Devices Required**:
- Conditional Button (purchase button)
- Item Granter (property key)
- Barrier Device (locked door)
- Trigger Device (unlock with key)

**Implementation**:
1. Place Conditional Button at property entrance: "Buy Property - $10,000"
2. Set condition: Requires 10,000 gold bars
3. On purchase success:
   - Deduct gold bars (handled by Conditional Button)
   - Grant unique property key item (Item Granter)
   - Display ownership confirmation (HUD Message)
4. Place Barrier Device at door
5. Add Trigger near door that checks for key item
6. If player has key → Disable Barrier (unlock door)

**Method 2: Class-Based Ownership**
**Devices Required**:
- Class Designer (ownership tracking)
- Conditional Button (purchase/access)
- Barrier Device (locked door)

**Implementation**:
1. Use Class Designer to create property ownership logic
2. On purchase: Set player class to "Owner of Property X"
3. Use Conditional Button with class requirement to access
4. This allows more complex systems (multiple owners, permissions)

### Property Customization

#### Interior Decoration
**Devices Required**:
- Prop Manipulator Device
- Button Devices (place/remove furniture)
- Barrier Devices (furniture placement zones)

**Implementation**:
1. Create "Edit Mode" button inside property
2. On activation → Enable Prop Manipulator
3. Allow player to place furniture from gallery
4. Save layout using Creative's built-in persistence (if available)

#### Property Zones
**Create Distinct Property Boundaries**:
1. Use Mutator Zone for private space
2. Set "No Damage" and "No Building" (if applicable)
3. Configure team permissions (only owner can edit)
4. Add Trigger to detect trespassing

---

## 🚗 Vehicle System

### Vehicle Spawning

#### Personal Vehicle Spawners
**Devices Required**:
- Vending Machine (vehicle purchase)
- Spawner Device (spawn vehicle)
- Button Device (call vehicle)
- Item Granter (vehicle key/license)

**Implementation**:
1. **Purchase Phase**:
   - Place Vending Machine at car dealership
   - Add vehicles: Car ($2,000), Sports Car ($15,000), SUV ($10,000)
   - On purchase → Grant vehicle key item
2. **Spawning Phase**:
   - Place Spawner Devices at parking lots and garages
   - Add Button: "Spawn Your Vehicle"
   - Set Conditional Button: Requires vehicle key item
   - On press → Spawn Device activates → Vehicle appears

#### Job Vehicle Spawners
**Devices Required**:
- Spawner Device (job vehicles)
- Conditional Button (team requirement)
- Timer Device (respawn delay)

**Implementation**:
1. Place Spawner at job headquarters
2. Add Button: "Request Police Car"
3. Set condition: Requires Police Team membership
4. On press → Spawn police vehicle
5. Connect Timer for 2-minute respawn delay (prevent spam)

**Job Vehicles**:
- **Police**: Patrol car, motorcycle, SWAT van
- **EMS**: Ambulance
- **Fire**: Fire truck
- **Taxi**: Taxi cab (company vehicle)
- **Delivery**: Cargo van

### Vehicle Damage & Repair

#### Implementing Damage
**Devices Required**:
- Damage Volume Device
- Mutator Zone (on vehicle)
- HUD Message (damage warning)

**Implementation** (Simplified):
1. Fortnite vehicles have built-in health
2. Use Damage Volume near hazards (walls, obstacles)
3. Display HUD warning when vehicle health low
4. Require repair at mechanic shop

#### Mechanic Shop
**Devices Required**:
- Button Device (repair service)
- Accolade Device (charge repair fee)
- HUD Message (repair confirmation)

**Implementation**:
1. Place Button at auto shop: "Repair Vehicle - $200"
2. On press → Deduct 200 gold bars
3. Respawn player's vehicle at full health (respawn vehicle)
4. Display confirmation message

### Fuel System (Optional)

#### Basic Fuel Mechanic
**Devices Required**:
- Timer Device (fuel consumption)
- Tracker Device (fuel gauge)
- Button Device (refuel at gas station)
- HUD Message (fuel level)

**Implementation**:
1. When player enters vehicle → Start Timer (fuel consumption)
2. Every minute → Reduce fuel level (tracked by Tracker Device)
3. Display fuel level on HUD
4. If fuel = 0 → Disable vehicle spawner (out of gas)
5. Refuel button at gas stations → Restore fuel for gold bars

---

## 🚨 Law Enforcement Mechanics

### Crime Detection System

#### Wanted Level System
**Devices Required**:
- Tracker Device (wanted level)
- Trigger Device (crime zones)
- HUD Message (wanted level display)
- Team Settings (police alerts)

**Implementation**:
1. Use Tracker Device to track wanted stars (0-5 scale)
2. When crime committed:
   - Player damages player → +1 wanted star
   - Player robs bank → +3 wanted stars
   - Player violates traffic law → +1 wanted star
3. Display wanted level on HUD for player and police
4. Connect to Trigger → If wanted player enters police station area → Alert police team

#### Traffic Violation Detection
**Devices Required**:
- Speed Boost Pad (to measure speeding)
- Trigger Device (red light zones)
- Timer Device (violation cooldown)
- HUD Message (ticket notification)

**Implementation**:
1. **Speeding Detection**:
   - Place Trigger on speed limit zones
   - If player velocity > threshold → Issue ticket (deduct gold bars)
2. **Red Light Running**:
   - Place Trigger at intersections
   - Use Timer to simulate red light (30 seconds)
   - If player passes through during red timer → Issue ticket
3. **Illegal Parking**:
   - Use Mutator Zones for no-parking areas
   - If player vehicle detected for > 2 minutes → Issue ticket

### Arrest System

#### Arrest Mechanics
**Devices Required**:
- Button Device (arrest button)
- Conditional Button (requires police team)
- Barrier Device (jail cell)
- Timer Device (jail time)
- HUD Message (arrest notification)

**Implementation**:
1. **Arrest Action**:
   - Police Officer approaches wanted player
   - Press arrest button (only available to police team)
   - Conditional Button checks: Player is within range AND has wanted level
2. **Transport to Jail**:
   - On successful arrest → Teleport player to jail cell
   - Remove player weapons (Item Remover Device)
   - Add Barrier to cell door (trap inside)
3. **Jail Time**:
   - Start Timer (5-30 minutes based on crime)
   - Display HUD: "Jail Time Remaining: XX:XX"
   - When timer ends → Remove Barrier → Release player
   - Reset wanted level to 0

#### Police Evidence System
**Devices Required**:
- Item Granter (evidence items)
- Button Device (collect evidence)
- Trigger Device (crime scene)

**Implementation** (Simplified):
1. When crime occurs → Spawn evidence item at location
2. Police use Button to collect evidence
3. Bring evidence to station → Process for bonus rewards

---

## 🎮 Performance Optimization

### Device Memory Management

#### Monitor Memory Usage
- Check memory bar in Creative Phone
- Current usage should stay below 80,000 (of 100,000 limit)
- Remove unnecessary devices
- Combine similar triggers into single devices

#### Optimization Tips
1. **Minimize Active Devices**:
   - Use multi-trigger devices instead of many single triggers
   - Disable devices when not in use
2. **Reduce Prop Count**:
   - Use galleries instead of individual props
   - Combine small props into prefabs
3. **Optimize Lighting**:
   - Limit dynamic lights
   - Use baked lighting where possible
4. **Simplify Device Logic**:
   - Use fewer channels (combine similar functions)
   - Avoid complex chain reactions
5. **Test Regularly**:
   - Play with max players (40) to test performance
   - Monitor frame rate drops in different areas

### Player Load Distribution

#### Spread Players Across Map
1. **Multiple Spawn Points**: Don't spawn all 40 players in one location
2. **Job Distribution**: Limit players per job (prevents overcrowding)
3. **District Boundaries**: Use triggers to load/unload areas dynamically (if possible)

### Network Performance

#### Reduce Network Load
1. **Limit Projectiles**: Don't spam explosive weapons
2. **Vehicle Limits**: Cap active vehicles at 20-30
3. **Prop Physics**: Minimize physics-enabled props
4. **Update Frequency**: Reduce HUD update frequency for non-critical info

---

## 🧪 Testing & Quality Assurance

### Pre-Launch Testing

#### Phase 1: Solo Testing
1. **Device Functionality**: Test all buttons, triggers, spawners
2. **Economy Balance**: Verify prices and salaries
3. **Job Systems**: Test each job's mechanics
4. **Property Access**: Ensure ownership works
5. **Vehicle Spawning**: Test all vehicle types

#### Phase 2: Small Group Testing (4-8 players)
1. **Multiplayer Interactions**: Test player-to-player systems
2. **Job Coordination**: Test emergency services and communication
3. **Economy Flow**: Monitor money earning/spending rates
4. **Police Arrests**: Test wanted and arrest systems
5. **Performance**: Check for lag or frame drops

#### Phase 3: Stress Testing (32-40 players)
1. **Max Capacity**: Fill server to max players
2. **Performance**: Monitor frame rate and lag
3. **Job Balance**: Ensure all jobs have players
4. **Device Load**: Check memory usage under stress
5. **Rule Enforcement**: Test admin/moderation tools

### Bug Tracking & Fixes

#### Common Issues & Solutions
1. **Players Stuck in Geometry**:
   - Fix: Add collision barriers
   - Add respawn buttons
2. **Device Not Triggering**:
   - Check channel connections
   - Verify team/class filters
   - Test trigger volume size
3. **Economy Exploits**:
   - Add cooldowns to money-granting devices
   - Limit duplicate purchases
   - Monitor gold bar inflation
4. **Vehicle Glitches**:
   - Add respawn timers
   - Limit active vehicle count
   - Add return-to-garage buttons
5. **Performance Issues**:
   - Reduce active devices
   - Optimize prop placement
   - Lower device update frequency

### Patch & Update Process

#### Regular Maintenance
1. **Weekly Checks**:
   - Monitor player feedback
   - Fix critical bugs
   - Adjust economy balance
2. **Monthly Updates**:
   - Add new content (jobs, vehicles, properties)
   - Major bug fixes
   - Performance improvements
3. **Seasonal Updates**:
   - New districts or expansions
   - Special events
   - Major feature additions

---

## 📚 Quick Reference

### Essential Device Channels Setup

#### Channel Organization
- **Channels 1-10**: Job systems (police, EMS, fire, etc.)
- **Channels 11-20**: Economy (salaries, purchases, banking)
- **Channels 21-30**: Property system (ownership, access)
- **Channels 31-40**: Vehicle system (spawning, repair)
- **Channels 41-50**: Law enforcement (arrests, wanted, crimes)
- **Channels 51-60**: Communication (radio, phone, announcements)
- **Channels 61-100**: General triggers and events
- **Channels 101-150**: Individual property access
- **Channels 151-200**: Reserved for future expansion

### Device Connection Examples

#### Example 1: Police Vehicle Spawner
```
Button Device: "Request Patrol Car"
↓ (Channel 31)
Conditional Device: Check if player on Police Team
↓ (Channel 32)
Spawner Device: Spawn Police Car
↓ (Channel 33)
Timer Device: 2-minute cooldown
```

#### Example 2: Salary Payment
```
Timer Device: 10-minute loop
↓ (Channel 11)
Trigger Device: Detect players in work zone
↓ (Channel 12)
Conditional Device: Check player team
↓ (Channel 13)
Accolade Device: Grant gold bars
↓ (Channel 14)
HUD Message: "Salary Paid: $150"
```

#### Example 3: Property Purchase
```
Button Device: "Buy House - $15,000"
↓ (Channel 21)
Conditional Button: Check gold bar balance
↓ (Channel 22)
Item Granter: Give property key
↓ (Channel 23)
HUD Message: "Congratulations! You own this property."
↓ (Channel 24)
Barrier Device: Unlock door (when key detected)
```

---

## 🎓 Advanced Tips

### Creating Immersive Environments
1. **Ambient Sound**: Use Audio Device for city ambiance
2. **Dynamic Lighting**: Time of day transitions
3. **Weather Effects**: Fog, rain (limited in Creative)
4. **NPC Simulation**: Use creature spawners as "AI civilians" (limited)

### Roleplay Enhancement
1. **Custom Emotes**: Assign job-specific emotes
2. **Visual Indicators**: Use glowing effects for on-duty jobs
3. **Job Uniforms**: Encourage players to wear appropriate skins
4. **Name Tags**: Use HUD to display job titles above players

### Admin Tools
1. **Spectator Mode**: Fly cam for monitoring
2. **Kick/Ban Buttons**: Admin-only buttons to remove players
3. **God Mode**: For admins during setup and fixes
4. **Quick Teleport**: Admin-only fast travel between districts

---

## 🆘 Troubleshooting Guide

### Issue: Device Memory Exceeds Limit
**Solutions**:
- Remove decorative props (keep functional devices)
- Combine multiple triggers into larger zones
- Use simpler device logic
- Remove unused devices

### Issue: Players Not Receiving Salary
**Solutions**:
- Check Timer Device is set to loop
- Verify Trigger covers work area
- Confirm Channel connections
- Test Accolade Device settings

### Issue: Vehicles Not Spawning
**Solutions**:
- Check Spawner Device configuration
- Verify vehicle gallery is loaded
- Increase spawn delay timer
- Clear spawn area of obstacles

### Issue: Property Doors Not Opening
**Solutions**:
- Check Barrier Device connections
- Verify key item granted on purchase
- Test Trigger Device placement (near door)
- Confirm Conditional Button settings

### Issue: Arrest System Not Working
**Solutions**:
- Check team filter on Conditional Button
- Verify wanted level tracked correctly
- Test teleport destination (jail cell)
- Confirm Barrier Device at jail door

---

## 📱 Phone System Implementation

### iFone 17 Pro Max Setup

The phone system is a central feature providing 9 integrated apps for player interaction. This section covers complete implementation.

#### Core Phone Infrastructure

**Devices Required**:
- **Item Granter Device** (phone item given to all players)
- **HUD Message Device** (display phone UI and app screens)
- **Multiple Button Devices** (app icons and navigation)
- **Conditional Button Devices** (feature requirements)
- **Trigger Devices** (detect phone usage)
- **Tracker Devices** (store data: contacts, streaks, balances)
- **Timer Devices** (streak counters, delivery times)

#### Phone Menu System

**Main Menu Implementation**:
1. Create **Phone Item** (consumable or tool item)
2. When used → Display HUD with 9 app icons
3. Each app icon = **Button Device**
4. Pressing app button → Opens app sub-menu

**Menu Layout** (3x3 Grid):
```
┌─────────┬─────────┬─────────┐
│ New X   │NewChat  │ Absher  │
├─────────┼─────────┼─────────┤
│ NewSab  │ Keeta   │ My Job  │
├─────────┼─────────┼─────────┤
│ Phone   │ Haraj   │ Newber  │
└─────────┴─────────┴─────────┘
```

### App 1: New X (Social Media)

**Implementation**:
1. **Post System**:
   - Button: "Create Post"
   - Input: Custom text prompt (140 chars)
   - Broadcast: HUD Message to all players
   - Channel 100: Post broadcast

2. **Feed Display**:
   - Scoreboard Device: Show recent posts
   - Refresh button updates feed
   - Like button increments counter

3. **Direct Messages**:
   - Conditional Button: Select recipient
   - HUD Message: Private message display
   - Channel 101-110: DM channels

**Devices Setup**:
```
Phone Item → Button "New X" → Sub-Menu
↓
Button "Create Post" → Text Input → Broadcast (Channel 100)
Button "View Feed" → Display Scoreboard
Button "DM" → Select Player → Send Message (Channel 101)
```

### App 2: New Chat (Messaging + Streaks)

**Streak System Implementation**:

**Devices Required**:
- **Tracker Device** (track streak count per player pair)
- **Timer Device** (24-hour reset check)
- **Accolade Device** (streak rewards)
- **HUD Message** (streak notifications)

**Implementation Steps**:
1. **Streak Counter**:
   ```
   Daily Timer (24 hours) → Check if message sent
   If YES: Increment Streak Counter (+1)
   If NO: Reset Streak to 0
   ```

2. **Messaging**:
   - Button: Select friend from list
   - Send message (text or "snap")
   - Updates last-contact timestamp
   - Message disappears after read (5 second HUD)

3. **Streak Display**:
   - Show flame icon + number next to friend name
   - HUD: "🔥 7 day streak with PlayerName!"
   
4. **Streak Rewards**:
   ```
   7 days: +100 social XP (Accolade Device)
   30 days: +500 XP + special badge
   100 days: +2000 XP + legendary badge
   ```

**Device Chain**:
```
Timer (24h loop) → Trigger (check message sent)
→ If true: Increment Streak (Tracker +1)
→ If false: Reset Streak (Tracker = 0)
→ Display Streak on HUD (HUD Message)
→ Check milestones → Grant rewards (Accolade)
```

### App 3: Absher (Government Services)

**Fine Payment System**:

**Devices Required**:
- **Tracker Device** (store outstanding fines)
- **Conditional Button** (pay fine - requires gold bars)
- **Accolade Device** (deduct payment)
- **HUD Message** (receipt confirmation)
- **Tracker Device** (store military rank for Police/SWAT) ⭐ **NEW**

**Implementation**:
1. **View Fines**:
   - Button: "My Violations"
   - Display Tracker value (total fines)
   - List violations with amounts

2. **Military Rank Display** ⭐ **NEW** (Police/SWAT Only):
   - Button: "View My Rank" (visible only to Police/SWAT)
   - Display rank information from Tracker:
     ```
     Button "View My Rank" (Conditional - Police/SWAT only)
     → Read Rank Tracker (1-17)
     → Read Force Type Tracker (1=Police, 2=SWAT)
     → Display Rank Info HUD:
       "════════════════════════════"
       "معلومات الرتبة العسكرية"
       "MILITARY RANK INFORMATION"
       "════════════════════════════"
       "الجهة: [Police/SWAT]"
       "الرتبة: [Rank Name in Arabic]"
       "الفئة: [Enlisted/Officers]"
       "الراتب: $[Amount]/hour"
       "رقم الرتبة: [X] من 17"
       "الرتبة التالية: [Next Rank]"
       "════════════════════════════"
     ```
   - Rank Tracker values:
     - 1-7: Enlisted ranks (أفراد)
     - 8-17: Officer ranks (ضباط)
   - Rank names by value:
     - 1: جندي | 2: جندي أول | 3: عريف
     - 4: وكيل رقيب | 5: رقيب | 6: رقيب أول
     - 7: رئيس رقباء | 8: ملازم | 9: ملازم أول
     - 10: نقيب | 11: رائد | 12: مقدم
     - 13: عقيد | 14: عميد | 15: لواء
     - 16: فريق | 17: فريق أول
   - Salary display from separate Tracker

3. **Pay Fine**:
   ```
   Button "Pay Fine" (Conditional)
   → Check gold bar balance
   → If sufficient: Deduct amount (Channel 120)
   → Clear violation from record
   → HUD: "Fine Paid: $200 LC"
   ```

4. **Identity Documents**:
   - Button: "Apply for ID"
   - Cost: $50 LC
   - Grant item: "City ID Card"
   - Required for certain jobs

5. **Police Integration**:
   - Police can add fines via special device
   - Trigger → Increment player's fine Tracker
   - Notification sent to player's phone

**Device Setup**:
```
Police Button "Issue Fine" → Input Amount
→ Target Player Selection
→ Tracker (add to player's fine total)
→ HUD Message (notify player)

Player Button "Pay Fine" (Conditional)
→ Check Balance (gold bars >= fine amount)
→ Accolade (deduct payment)
→ Tracker (reset fine to 0)

Military Rank Display (NEW):
→ Conditional Button (visible to Police/SWAT only)
→ Read Rank Tracker (1-17)
→ Read Force Tracker (1=Police, 2=SWAT)  
→ HUD Message (display formatted rank info)
→ Auto-calculate salary from rank
```

### App 4: NewSab (WhatsApp Clone)

**Group Chat Implementation**:

**Devices Required**:
- **Multiple HUD Message Devices** (separate channels per group)
- **Button Devices** (send message, create group)
- **Tracker Device** (group member lists)

**Implementation**:
1. **Create Group**:
   - Button: "New Group"
   - Select up to 10 players
   - Assign group to Channel (130-140)

2. **Send Message**:
   - Select group or individual
   - Text input
   - Broadcast on group's channel
   - All members see HUD message

3. **Read Receipts**:
   - Track who viewed message
   - Blue checkmark after read
   - Uses Trigger Device (detect view)

**Device Chain**:
```
Button "Send Message"
→ Select Recipient/Group
→ Text Input
→ Broadcast on Channel (130+)
→ HUD Message to recipients
→ Track Read Status (Trigger)
```

### App 5: Keeta (Food Delivery)

**Order & Delivery System**:

**Devices Required**:
- **Vending Machine** (restaurant menus)
- **Spawner Device** (spawn food items)
- **Button Device** (order placement)
- **Accolade Device** (payment processing)
- **Timer Device** (delivery countdown)
- **Item Granter** (grant food to player)

**Implementation**:
1. **Restaurant Menu**:
   - Each restaurant = Vending Machine
   - Items: Pizza ($15), Burger ($10), Drink ($5)
   - Player selects items

2. **Order Placement**:
   ```
   Button "Place Order"
   → Check balance (Conditional)
   → Deduct payment (Accolade)
   → Alert delivery drivers (HUD broadcast Channel 145)
   → Start delivery timer (5-10 minutes)
   ```

3. **Driver Acceptance**:
   - Drivers see order notification
   - Button: "Accept Delivery"
   - Navigate to restaurant → Pick up → Deliver to player
   - Earn fare + tip

4. **Food Delivery**:
   - Timer ends → Item Granter gives food to player
   - Food provides health boost (if applicable)
   - Player can rate driver

**Device Setup**:
```
Vending Machine (Menu) → Player selects items
→ Button "Order" (Conditional - check balance)
→ Accolade (deduct cost)
→ HUD (notify drivers on Channel 145)
→ Driver accepts → Navigate to pickup
→ Timer (delivery countdown)
→ Item Granter (give food to player)
→ Accolade (pay driver + tip)
```

### App 6: My Job (Employment Platform)

**Job Listing System**:

**Devices Required**:
- **HUD Message Device** (display job listings)
- **Button Devices** (post job, apply)
- **Conditional Button** (check requirements)
- **Tracker Device** (application status)

**Implementation**:
1. **View Jobs**:
   - Button: "Browse Jobs"
   - Display available positions
   - Filter by: salary, type, level required

2. **Apply for Job**:
   ```
   Button "Apply" (Conditional)
   → Check player level
   → Check requirements met
   → Submit application (Tracker)
   → Notify employer (HUD)
   ```

3. **Employer Posting** (for business owners):
   - Button: "Post Job"
   - Input: Title, salary, requirements
   - Add to job board
   - Receive applications

4. **Job Acceptance**:
   - Employer reviews applications
   - Button: "Hire Player"
   - Player joins team/gets equipment
   - Integration with Employment Center

**Device Chain**:
```
Business Owner Button "Post Job"
→ Input job details
→ Add to Job Board (Scoreboard)

Player Button "Apply"
→ Conditional (check level/requirements)
→ Tracker (mark as applied)
→ HUD (notify employer)

Employer Button "Hire"
→ Team Settings (assign player to job team)
→ Item Granter (give equipment)
→ HUD (notify player of acceptance)
```

### App 7: Phone (Native Dialer)

**Call System Implementation**:

**Devices Required**:
- **Button Device** (contacts list)
- **HUD Message** (incoming call notification)
- **Trigger Device** (detect answer/decline)
- **Audio Device** (ringtone)
- **Proximity Chat** (for voice calls)

**Implementation**:
1. **Contact Management**:
   - Button: "Add Contact"
   - Input: Player name + number
   - Store in player's contact list

2. **Make Call**:
   ```
   Button "Call Contact"
   → Select from list
   → HUD to recipient (incoming call)
   → Recipient buttons: "Answer" / "Decline"
   → If answered: Open voice/text chat
   ```

3. **Call Types**:
   - Voice: Uses proximity chat or party chat
   - Text: HUD message exchange
   - Emergency (911): Direct to dispatch

4. **Voicemail**:
   - If declined/unanswered
   - Button: "Leave Voicemail"
   - Text message stored for recipient
   - Notification on next login

**Device Setup**:
```
Button "Call" → Select Contact
→ HUD Message (recipient - incoming call)
→ Buttons: "Answer" / "Decline"

If Answer:
→ Enable voice chat / text chat
→ Timer (call duration tracking)

If Decline:
→ Button "Voicemail" (caller)
→ Store message (Tracker)
→ Notify on recipient login
```

### App 8: Haraj (Vehicle Marketplace)

**Buy/Sell System**:

**Devices Required**:
- **Vending Machine** (vehicle listings)
- **Button Device** (list vehicle, contact seller)
- **Conditional Button** (purchase - requires funds)
- **Accolade Device** (process transaction)
- **Spawner Device** (spawn purchased vehicle)
- **Item Granter** (give vehicle key)

**Implementation**:
1. **List Vehicle for Sale**:
   ```
   Button "Sell My Vehicle"
   → Input: Vehicle type, price, condition
   → Add to marketplace (Vending Machine)
   → 5% listing fee deducted
   ```

2. **Browse Vehicles**:
   - Display all listed vehicles
   - Filter: Type (sedan, sports, SUV)
   - Filter: Price range
   - Sort: Newest, price low-high

3. **Purchase Vehicle**:
   ```
   Button "Buy Vehicle" (Conditional)
   → Check balance (price + 5% fee)
   → Deduct from buyer (Accolade)
   → Pay seller 95% (Accolade)
   → Grant vehicle key (Item Granter)
   → Remove from marketplace
   ```

4. **Meet & Trade**:
   - Button: "Contact Seller"
   - Arrange meeting location
   - Complete transaction in person
   - Safety: Recommend police station meetups

**Device Chain**:
```
Seller Button "List Vehicle"
→ Input price and details
→ Accolade (deduct 5% fee)
→ Add to Vending Machine

Buyer Button "Buy" (Conditional)
→ Check gold bars >= price
→ Accolade (deduct from buyer)
→ Accolade (pay seller 95%)
→ Item Granter (give vehicle key)
→ Spawner (spawn vehicle at location)
→ Remove listing
```

### App 9: Newber (Ride-Hailing)

**Uber-Style Ride System**:

**Devices Required**:
- **Button Device** (request ride, accept ride)
- **HUD Message** (driver notifications, ride status)
- **Trigger Device** (detect pickup/dropoff locations)
- **Timer Device** (estimate arrival time)
- **Accolade Device** (fare payment)
- **Tracker Device** (driver ratings)

**Implementation**:
1. **Request Ride**:
   ```
   Button "Request Newber"
   → Select destination (from list or map)
   → Calculate fare estimate
   → Broadcast to drivers (Channel 150)
   → HUD: "Finding driver..."
   ```

2. **Driver Accepts**:
   - Nearby drivers see notification
   - Button: "Accept Ride"
   - First to accept gets job
   - Display pickup location

3. **Ride Progress**:
   ```
   Driver navigates to pickup
   → Trigger at pickup location
   → HUD: "Driver arrived!"
   → Player enters vehicle (proximity)
   → Driver navigates to destination
   → Trigger at destination
   → Ride complete
   ```

4. **Payment & Rating**:
   ```
   Ride ends:
   → Calculate distance-based fare
   → Accolade (deduct from passenger)
   → Accolade (pay driver + tip option)
   → Buttons: Rate driver (1-5 stars)
   → Update driver rating (Tracker)
   ```

5. **Pricing**:
   - Base fare: $10 LC
   - Per distance unit: $2 LC
   - Surge pricing during peak hours: 1.5x

**Driver Side Implementation**:
```
Button "Go Online" (driver app)
→ Receive ride requests (HUD Channel 150)
→ Button "Accept"
→ Navigate to pickup (waypoint)
→ Trigger (pickup zone) → "Passenger picked up"
→ Navigate to destination
→ Trigger (destination) → "Ride complete"
→ Accolade (receive payment + tip)
→ Rating from passenger (Tracker)
```

**Passenger Side Implementation**:
```
Button "Request Ride"
→ Select destination
→ Fare estimate displayed
→ Wait for driver acceptance
→ HUD: Driver name, ETA, vehicle
→ Trigger (driver arrives) → Enter vehicle
→ Trigger (destination) → Exit vehicle
→ Accolade (auto-deduct fare)
→ Button "Rate Driver" (1-5 stars)
→ Button "Add Tip" (optional $5-20)
```

### App 10: Masraf Al Rajhi (مصرف الراجحي - Banking App)

**Complete Banking System Implementation**:

**Devices Required**:
- **HUD Message Device** (display balance, transaction history)
- **Button Device** (transfer money, view history, menu navigation)
- **Conditional Button** (check balance before transfers)
- **Accolade Device** (process money transfers and deposits)
- **Tracker Device** (store transaction history, account balances)
- **Timer Device** (salary deposit automation)
- **Item Granter** (visual bank card item)

**Implementation**:

1. **Account Balance Display**:
   ```
   Button "Open Masraf Al Rajhi"
   → Tracker (read player's New Coins balance)
   → HUD Message: "Balance: [Amount] LC"
   → Display account number (Player ID)
   → Display account holder name
   → Show last transaction date/time
   ```

2. **Money Transfer System**:
   ```
   Button "Transfer Money"
   → Input: Recipient name or account number
   → Input: Transfer amount
   → HUD: Recipient details confirmation
   → Conditional Button (check sender balance >= amount)
   
   If balance sufficient:
   → Button "Confirm Transfer"
   → Accolade (deduct from sender: -amount)
   → Accolade (add to recipient: +amount)
   → Tracker (log transaction for both players)
   → HUD (sender): "Transfer successful to [Name]"
   → HUD (recipient): "Received [Amount] LC from [Name]"
   → Push notification to recipient phone
   
   If insufficient balance:
   → HUD: "Insufficient funds. Balance: [Amount]"
   → Button "Cancel"
   ```

3. **Salary Receipt System**:
   ```
   Timer Device (hourly salary automation)
   → Trigger every game hour
   → Check player's job from Job Manager
   → Calculate salary based on job
   
   Salary Deposit:
   → Accolade (add salary amount to player)
   → Tracker (log transaction)
   → HUD: "Salary deposited: [Amount] LC from [Employer]"
   → Push notification: "💰 Salary received!"
   → Update balance display in real-time
   
   Bank App View:
   → Button "View Salary Info"
   → HUD: "Last Salary: [Amount] on [Date]"
   → HUD: "Next Salary: [Time]"
   → HUD: "Job: [Title] | Employer: [Name]"
   → HUD: "Salary Rate: [Amount]/hour"
   ```

4. **Transaction History System**:
   ```
   Button "Transaction History"
   → Tracker (retrieve last 50 transactions)
   
   Display format:
   ┌─────────────────────────────────────────┐
   │ Date/Time | Type      | Amount | Balance│
   ├─────────────────────────────────────────┤
   │ 12/27 3:45PM | Salary   | +$200 | $1,450│
   │ 12/27 3:30PM | Transfer | -$50  | $1,250│
   │ 12/27 3:15PM | Deposit  | +$100 | $1,300│
   │ 12/27 3:00PM | Payment  | -$75  | $1,200│
   └─────────────────────────────────────────┘
   
   For each transaction:
   → Show transaction ID
   → Show type (Salary/Transfer/Payment/Deposit)
   → Show amount (+ for credit, - for debit)
   → Show running balance after transaction
   → Show recipient/sender name (if transfer)
   → Show description/notes
   
   Filters:
   → Button "Filter by Date" (last 7/30/90 days)
   → Button "Filter by Type" (all/transfers/salary/payments)
   → Button "Export Statement" (save to player data)
   ```

5. **Additional Banking Features**:
   
   **Bill Payments**:
   ```
   Button "Pay Bills"
   → Display bills list (fines from Absher, utilities)
   → Select bill to pay
   → Conditional (check balance)
   → Accolade (deduct amount)
   → HUD: "Bill paid successfully"
   → Update Absher app (clear fine)
   ```
   
   **Loan Services**:
   ```
   Button "Loan Application"
   → Check player level and job status
   → Calculate loan eligibility (max 3x weekly salary)
   → Display loan terms (interest rate, duration)
   → Button "Apply"
   → Tracker (mark loan active)
   → Accolade (deposit loan amount)
   → Timer (weekly repayment auto-deduct)
   ```
   
   **Savings Goals**:
   ```
   Button "Set Savings Goal"
   → Input target amount and name
   → Tracker (store goal)
   → HUD: Show progress bar
   → Optional auto-transfer % of salary to savings
   ```

6. **Security & Notifications**:
   ```
   Security PIN Setup:
   → Button "Set PIN"
   → Input 4-digit code
   → Tracker (store encrypted PIN)
   → Required for transfers over $500
   
   Push Notifications:
   → Low balance warning (<$100 LC)
   → Salary deposit alerts
   → Transfer received alerts
   → Large withdrawal alerts (>$1000)
   → Suspicious activity warnings
   ```

**Integration with Other Apps**:

```
Payment Integration:
→ Absher: Pay fines via Masraf Al Rajhi
→ Keeta: Food payment deducted from bank balance
→ Newber: Ride fare auto-deducted from account
→ Haraj: Vehicle purchase payment through bank
→ ATMs: Cash withdrawal syncs with app balance
→ Stores: Purchase payments tracked in history

Salary Integration:
→ Job System → Timer → Masraf Al Rajhi Deposit
→ All job salaries automatically deposited
→ Real-time balance updates
→ Employer name shown in transaction
```

**Channel Allocation**:
- Channel 165: Bank balance updates
- Channel 166: Transfer notifications
- Channel 167: Salary deposits
- Channel 168: Transaction logging

**Device Chain Example**:
```
Player Opens Bank App
↓
Button Device (Main Menu)
├── Button "View Balance"
│   └→ Tracker → HUD (display balance)
├── Button "Transfer Money"
│   ├→ Input recipient & amount
│   ├→ Conditional (check balance)
│   └→ Accolade (process transfer)
├── Button "Transaction History"
│   └→ Tracker → HUD (display last 20)
├── Button "Salary Info"
│   └→ HUD (display job & next payment)
└── Button "Pay Bills"
    └→ Link to Absher fines
    
Background Process:
Timer (hourly) → Check jobs → Accolade (salary) → Notification
```

**Realistic Saudi Banking Theme**:
- Masraf Al Rajhi green color scheme (#00853E)
- Arabic/English bilingual interface
- Islamic banking terminology (no interest, profit-sharing)
- Traditional Saudi financial features
- Prayer time reminders
- Zakat calculator

**Memory Allocation**: ~8,000 memory (for transaction tracking)


### Phone System Device Budget

**Memory Allocation**:
- Phone UI System: ~5,000 memory
- Per App System: ~2,000-3,000 memory each
- Total Phone System: ~25,000 memory (25% of budget)

**Channel Allocation**:
- Channels 100-110: New X (posts, DMs)
- Channels 111-120: New Chat (messages, streaks)
- Channels 121-130: Absher (government services)
- Channels 131-140: NewSab (group chats)
- Channels 141-145: Keeta (food orders)
- Channels 146-150: My Job (applications)
- Channels 151-155: Phone (calls)
- Channels 156-160: Haraj (vehicle sales)
- Channels 161-165: Newber (ride requests)

### Testing Phone System

**Test Checklist**:
- [ ] Phone item spawns for all players
- [ ] All 9 apps accessible from main menu
- [ ] New X posts broadcast to all players
- [ ] New Chat streaks increment daily
- [ ] Absher fines can be paid
- [ ] NewSab messages reach recipients
- [ ] Keeta orders trigger delivery jobs
- [ ] My Job listings display correctly
- [ ] Phone calls connect players
- [ ] Haraj transactions complete successfully
- [ ] Newber rides calculate fares correctly

**Common Issues & Solutions**:
1. **Apps not opening**: Check HUD Message channel conflicts
2. **Payments failing**: Verify Accolade Device settings and balance
3. **Streaks not counting**: Check Timer Device 24-hour loop
4. **Notifications not showing**: Check HUD Message display time
5. **Calls not connecting**: Verify proximity chat settings

---

## 📖 Additional Resources

### Fortnite Creative Tutorials
- **Epic Games Creative Documentation**: Official guides
- **YouTube**: "Fortnite Creative Device Tutorials"
- **Community Forums**: r/FortniteCreative

### Roleplay Server Guides
- **FiveM Documentation**: Learn roleplay systems
- **NoPixel Wiki**: Study roleplay mechanics
- **Roleplay Guidelines**: Best practices

---

<div align="center">

**New Live - Technical Guide**  
Version 1.0 | December 2025

*Build Your City. Live Your Story.*

</div>
