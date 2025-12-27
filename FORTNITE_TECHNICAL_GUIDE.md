# City of Legends - Technical Implementation Guide

## 📋 Table of Contents
1. [Fortnite Creative Basics](#fortnite-creative-basics)
2. [Device Setup](#device-setup)
3. [Economy System](#economy-system)
4. [Job System Implementation](#job-system-implementation)
5. [Property System](#property-system)
6. [Vehicle System](#vehicle-system)
7. [Law Enforcement Mechanics](#law-enforcement-mechanics)
8. [Performance Optimization](#performance-optimization)
9. [Testing & Quality Assurance](#testing--quality-assurance)

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

#### Using Gold Bars as "Legend Coins"
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

**City of Legends - Technical Guide**  
Version 1.0 | December 2025

*Build Your City. Live Your Story.*

</div>
