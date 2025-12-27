# City of Legends - Unreal Engine Implementation Guide

## 🎮 UEFN (Unreal Editor for Fortnite) Development

This guide covers implementing "City of Legends" using **Unreal Engine 5** with **UEFN (Unreal Editor for Fortnite)** for full programming control, instead of basic Creative devices.

---

## 📋 Table of Contents
1. [UEFN vs Creative Mode](#uefn-vs-creative-mode)
2. [Development Setup](#development-setup)
3. [Verse Programming Language](#verse-programming-language)
4. [Core Systems Implementation](#core-systems-implementation)
5. [Economy System (Verse)](#economy-system-verse)
6. [Job System (Verse)](#job-system-verse)
7. [Phone System (Verse)](#phone-system-verse)
8. [Property System (Verse)](#property-system-verse)
9. [Vehicle System (Verse)](#vehicle-system-verse)
10. [Multiplayer & Networking](#multiplayer--networking)

---

## 🆚 UEFN vs Creative Mode

### Why Use UEFN?

| Feature | Fortnite Creative | UEFN (Unreal Engine) |
|---------|-------------------|----------------------|
| **Programming** | Device-based logic only | Full Verse scripting + Blueprints |
| **Customization** | Limited to pre-built devices | Complete custom gameplay |
| **UI/UX** | Basic HUD messages | Custom UI with Slate/UMG |
| **Data Storage** | Limited tracking | Persistent data with databases |
| **Performance** | Device memory limits | Optimized code execution |
| **Complexity** | Simple systems | Complex game mechanics |
| **Learning Curve** | Easy | Moderate (requires programming) |

### UEFN Advantages for City of Legends

✅ **Custom Phone UI** - Real smartphone interface with touch interactions  
✅ **Advanced Economy** - Complex transactions, stock market, business logic  
✅ **Persistent Data** - Save player progress, streaks, property ownership  
✅ **AI Systems** - NPC civilians, traffic, smart enemies  
✅ **Dynamic Events** - Weather, time of day, random events  
✅ **Professional Tools** - Version control, debugging, profiling  

---

## 🛠️ Development Setup

### Prerequisites

1. **Epic Games Launcher** - Download and install
2. **Unreal Engine 5.4+** - Install from Epic launcher
3. **UEFN (Unreal Editor for Fortnite)** - Install from Epic launcher
4. **Visual Studio Code** - Recommended IDE for Verse
5. **Git** - For version control (optional but recommended)

### Installation Steps

```bash
# 1. Install Epic Games Launcher
# Download from: https://www.epicgames.com/store/download

# 2. Install UEFN from Epic Launcher
# Open Epic Games Launcher → Unreal Engine → UEFN

# 3. Install Visual Studio Code
# Download from: https://code.visualstudio.com/

# 4. Install Verse Language Extension
# In VS Code: Extensions → Search "Verse" → Install
```

### Project Setup

1. **Create New UEFN Project**:
   - Open UEFN
   - File → New Project
   - Select "Blank" template
   - Name: "CityOfLegends"
   - Location: Choose your project directory
   - Click "Create"

2. **Project Structure**:
```
CityOfLegends/
├── Content/
│   ├── Maps/
│   │   ├── AlMarkaz/
│   │   ├── PaletoBay/
│   │   └── SandyShores/
│   ├── Blueprints/
│   │   ├── Characters/
│   │   ├── Vehicles/
│   │   └── Systems/
│   ├── UI/
│   │   ├── Phone/
│   │   ├── HUD/
│   │   └── Menus/
│   └── Scripts/
│       └── Verse/
├── Plugins/
└── Config/
```

---

## 📝 Verse Programming Language

### What is Verse?

**Verse** is Epic Games' new programming language designed for UEFN and Unreal Engine, providing:
- Type-safe, functional programming
- Concurrent execution
- Built-in multiplayer support
- Integration with Unreal Engine systems

### Basic Verse Syntax

```verse
# Hello World in Verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }

hello_world := class(creative_device):
    
    @editable
    MessageDevice : hud_message_device = hud_message_device{}
    
    OnBegin<override>()<suspends>:void=
        MessageDevice.SetText("Welcome to City of Legends!")
        MessageDevice.Show(AllPlayers)
```

### Key Verse Concepts

```verse
# Variables
var PlayerMoney : int = 2000
const TaxRate : float = 0.05

# Functions
CalculateTax(Amount : float) : float =
    Amount * TaxRate

# Classes
player_data := class:
    var Name : string
    var Money : int
    var Level : int
    
    GetMoney() : int =
        Money

# Arrays/Maps
var PlayerList : []player = array{}
var PropertyOwners : [string]player = map{}
```

---

## 🎮 Core Systems Implementation

### Game Manager (Main System)

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

city_of_legends_manager := class(creative_device):
    
    # System References
    @editable
    EconomySystem : economy_manager = economy_manager{}
    
    @editable
    JobSystem : job_manager = job_manager{}
    
    @editable
    PhoneSystem : phone_manager = phone_manager{}
    
    @editable
    PropertySystem : property_manager = property_manager{}
    
    # Player Management
    var Players : [player]player_data = map{}
    
    # Initialization
    OnBegin<override>()<suspends>:void=
        Print("City of Legends - Initializing...")
        
        # Start all systems
        EconomySystem.Initialize()
        JobSystem.Initialize()
        PhoneSystem.Initialize()
        PropertySystem.Initialize()
        
        # Listen for player events
        GetPlayspace().PlayerAddedEvent().Subscribe(OnPlayerJoined)
        GetPlayspace().PlayerRemovedEvent().Subscribe(OnPlayerLeft)
        
        Print("City of Legends - Ready!")
    
    # Player Events
    OnPlayerJoined(Player : player):void=
        Print("Player joined: {Player}")
        
        # Create player data
        NewPlayerData := player_data{
            Name := "Player",
            Money := 2000,
            Level := 1
        }
        
        set Players[Player] = NewPlayerData
        
        # Give starter items
        EconomySystem.GiveStartingMoney(Player, 2000)
        PhoneSystem.GivePhone(Player)
        
        # Show welcome message
        ShowWelcomeMessage(Player)
    
    OnPlayerLeft(Player : player):void=
        Print("Player left: {Player}")
        
        # Save player data before removing
        if (PlayerData := Players[Player]):
            SavePlayerData(Player, PlayerData)
        
        # Remove from active players
        if (set Players[Player] = false) {}
    
    ShowWelcomeMessage(Player : player):void=
        # Display welcome UI
        Print("Welcome to City of Legends, {Player}!")
```

---

## 💰 Economy System (Verse)

### Economy Manager

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }

economy_manager := class(creative_device):
    
    # Currency tracking
    var PlayerBalances : [player]int = map{}
    
    # Transaction history
    var TransactionLog : []transaction = array{}
    
    # UI References
    @editable
    BalanceHUD : hud_message_device = hud_message_device{}
    
    Initialize():void=
        Print("Economy System - Initialized")
    
    # Give money to player
    GiveMoney(Player : player, Amount : int)<suspends>:void=
        if (CurrentBalance := PlayerBalances[Player]):
            set PlayerBalances[Player] = CurrentBalance + Amount
        else:
            set PlayerBalances[Player] = Amount
        
        # Update UI
        UpdateBalanceDisplay(Player)
        
        # Log transaction
        LogTransaction(Player, "Credit", Amount)
    
    # Take money from player
    TakeMoney(Player : player, Amount : int)<suspends>:bool=
        if (CurrentBalance := PlayerBalances[Player]):
            if (CurrentBalance >= Amount):
                set PlayerBalances[Player] = CurrentBalance - Amount
                UpdateBalanceDisplay(Player)
                LogTransaction(Player, "Debit", Amount)
                return true
        return false
    
    # Check if player has enough money
    HasMoney(Player : player, Amount : int):bool=
        if (Balance := PlayerBalances[Player]):
            return Balance >= Amount
        return false
    
    # Get player balance
    GetBalance(Player : player):int=
        if (Balance := PlayerBalances[Player]):
            return Balance
        return 0
    
    # Transfer money between players
    Transfer(FromPlayer : player, ToPlayer : player, Amount : int)<suspends>:bool=
        if (HasMoney(FromPlayer, Amount)):
            TakeMoney(FromPlayer, Amount).Await()
            GiveMoney(ToPlayer, Amount).Await()
            return true
        return false
    
    # Update balance display
    UpdateBalanceDisplay(Player : player):void=
        Balance := GetBalance(Player)
        BalanceHUD.SetText("Balance: ${Balance} LC")
        BalanceHUD.Show(Player)
    
    # Transaction logging
    LogTransaction(Player : player, Type : string, Amount : int):void=
        NewTransaction := transaction{
            Player := Player,
            Type := Type,
            Amount := Amount,
            Timestamp := GetCurrentTime()
        }
        set TransactionLog += array{NewTransaction}
    
    # Starter money
    GiveStartingMoney(Player : player, Amount : int):void=
        set PlayerBalances[Player] = Amount
        UpdateBalanceDisplay(Player)

# Transaction data structure
transaction := struct:
    Player : player
    Type : string
    Amount : int
    Timestamp : float
```

### Salary Payment System

```verse
salary_system := class(creative_device):
    
    @editable
    PaymentInterval : float = 600.0  # 10 minutes
    
    @editable
    EconomyManager : economy_manager = economy_manager{}
    
    @editable
    JobManager : job_manager = job_manager{}
    
    OnBegin<override>()<suspends>:void=
        # Start salary payment loop
        loop:
            Sleep(PaymentInterval)
            PayAllSalaries()
    
    PayAllSalaries()<suspends>:void=
        # Get all players with jobs
        AllPlayers := GetPlayspace().GetPlayers()
        
        for (Player : AllPlayers):
            if (Job := JobManager.GetPlayerJob(Player)):
                Salary := JobManager.GetJobSalary(Job)
                
                # Pay salary
                EconomyManager.GiveMoney(Player, Salary)
                
                # Notify player
                Print("Salary paid: ${Salary} LC to {Player}")
```

---

## 👔 Job System (Verse)

### Job Manager

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }

job_manager := class(creative_device):
    
    # Job data
    var PlayerJobs : [player]string = map{}
    var JobSalaries : [string]int = map{}
    
    # Team devices
    @editable
    PoliceTeam : team_settings_and_inventory_device = team_settings_and_inventory_device{}
    
    @editable
    EMSTeam : team_settings_and_inventory_device = team_settings_and_inventory_device{}
    
    Initialize():void=
        # Define job salaries
        set JobSalaries["Police"] = 200
        set JobSalaries["EMS"] = 150
        set JobSalaries["Fire"] = 150
        set JobSalaries["Taxi"] = 100
        set JobSalaries["Business"] = 150
        set JobSalaries["Retail"] = 100
        
        Print("Job System - Initialized")
    
    # Assign job to player
    AssignJob(Player : player, JobName : string)<suspends>:void=
        set PlayerJobs[Player] = JobName
        
        # Switch to job team
        if (JobName = "Police"):
            PoliceTeam.SetTeam(Player, 1)
            GivePoliceEquipment(Player)
        else if (JobName = "EMS"):
            EMSTeam.SetTeam(Player, 2)
            GiveEMSEquipment(Player)
        
        Print("{Player} assigned to {JobName}")
    
    # Get player's current job
    GetPlayerJob(Player : player):?string=
        PlayerJobs[Player]
    
    # Get job salary
    GetJobSalary(JobName : string):int=
        if (Salary := JobSalaries[JobName]):
            return Salary
        return 0
    
    # Give job equipment
    GivePoliceEquipment(Player : player):void=
        # Grant police items (weapons, badge, etc.)
        Print("Giving police equipment to {Player}")
    
    GiveEMSEquipment(Player : player):void=
        # Grant medical items
        Print("Giving medical equipment to {Player}")
```

---

## 📱 Phone System (Verse)

### Phone Manager

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/UI }

phone_manager := class(creative_device):
    
    # Phone UI instances
    var PhoneUIs : [player]phone_ui = map{}
    
    # App managers
    @editable
    NewXApp : new_x_app = new_x_app{}
    
    @editable
    NewChatApp : new_chat_app = new_chat_app{}
    
    @editable
    AbsherApp : absher_app = absher_app{}
    
    Initialize():void=
        Print("Phone System - Initialized")
    
    # Give phone to player
    GivePhone(Player : player)<suspends>:void=
        # Create phone UI
        NewPhoneUI := phone_ui{}
        set PhoneUIs[Player] = NewPhoneUI
        
        # Initialize apps
        NewPhoneUI.AddApp("New X", NewXApp)
        NewPhoneUI.AddApp("New Chat", NewChatApp)
        NewPhoneUI.AddApp("Absher", AbsherApp)
        
        Print("Phone given to {Player}")
    
    # Open phone for player
    OpenPhone(Player : player):void=
        if (PhoneUI := PhoneUIs[Player]):
            PhoneUI.Show(Player)

# Phone UI class
phone_ui := class:
    var Apps : [string]phone_app = map{}
    
    AddApp(Name : string, App : phone_app):void=
        set Apps[Name] = App
    
    Show(Player : player):void=
        # Display phone UI to player
        Print("Showing phone to {Player}")
    
    Hide(Player : player):void=
        # Hide phone UI
        Print("Hiding phone from {Player}")

# Base phone app class
phone_app := class:
    Open(Player : player):void=
        Print("Opening app for {Player}")
```

### New Chat App (with Streaks)

```verse
new_chat_app := class(phone_app):
    
    # Streak tracking
    var PlayerStreaks : [player][player]int = map{}
    var LastMessage : [player][player]float = map{}
    
    Open<override>(Player : player):void=
        Print("Opening New Chat for {Player}")
        ShowFriendList(Player)
    
    # Send snap to friend
    SendSnap(FromPlayer : player, ToPlayer : player, Message : string)<suspends>:void=
        # Update last message time
        CurrentTime := GetCurrentTime()
        
        if (PlayerMessages := LastMessage[FromPlayer]):
            set PlayerMessages[ToPlayer] = CurrentTime
        
        # Check and update streak
        UpdateStreak(FromPlayer, ToPlayer)
        
        # Deliver message
        DeliverSnap(ToPlayer, FromPlayer, Message)
    
    # Update streak counter
    UpdateStreak(Player1 : player, Player2 : player):void=
        # Get current streak
        if (Streaks := PlayerStreaks[Player1]):
            if (CurrentStreak := Streaks[Player2]):
                # Increment streak
                set Streaks[Player2] = CurrentStreak + 1
                
                # Check for rewards
                CheckStreakRewards(Player1, CurrentStreak + 1)
            else:
                # Start new streak
                set Streaks[Player2] = 1
    
    # Check and give streak rewards
    CheckStreakRewards(Player : player, Streak : int):void=
        if (Streak = 7):
            # 7-day streak reward
            Print("{Player} reached 7-day streak! +100 XP")
        else if (Streak = 30):
            # 30-day streak reward
            Print("{Player} reached 30-day streak! +500 XP")
        else if (Streak = 100):
            # 100-day streak reward
            Print("{Player} reached 100-day streak! +2000 XP")
    
    ShowFriendList(Player : player):void=
        # Display friend list UI
        Print("Showing friend list to {Player}")
    
    DeliverSnap(ToPlayer : player, FromPlayer : player, Message : string):void=
        # Show snap notification
        Print("Snap from {FromPlayer} to {ToPlayer}: {Message}")

GetCurrentTime():float=
    # Return current game time
    0.0
```

### Newber App (Ride-Hailing)

```verse
newber_app := class(phone_app):
    
    # Active rides
    var ActiveRides : [player]ride_request = map{}
    var OnlineDrivers : []player = array{}
    
    Open<override>(Player : player):void=
        Print("Opening Newber for {Player}")
        ShowMainMenu(Player)
    
    # Request a ride
    RequestRide(Passenger : player, Destination : vector3)<suspends>:void=
        # Calculate fare
        CurrentLocation := GetPlayerLocation(Passenger)
        Distance := CalculateDistance(CurrentLocation, Destination)
        Fare := CalculateFare(Distance)
        
        # Create ride request
        NewRide := ride_request{
            Passenger := Passenger,
            Destination := Destination,
            Fare := Fare
        }
        
        # Notify nearby drivers
        NotifyDrivers(NewRide)
        
        set ActiveRides[Passenger] = NewRide
    
    # Driver accepts ride
    AcceptRide(Driver : player, Passenger : player)<suspends>:void=
        if (Ride := ActiveRides[Passenger]):
            # Assign driver to ride
            set Ride.Driver = Driver
            
            # Notify both players
            Print("Driver {Driver} accepted ride for {Passenger}")
    
    # Complete ride
    CompleteRide(Passenger : player, Driver : player)<suspends>:void=
        if (Ride := ActiveRides[Passenger]):
            # Process payment
            # EconomyManager.Transfer(Passenger, Driver, Ride.Fare)
            
            # Rate driver
            ShowRatingUI(Passenger, Driver)
            
            # Remove active ride
            if (set ActiveRides[Passenger] = false) {}
    
    CalculateFare(Distance : float):int=
        BaseFare := 10
        PerDistanceRate := 2
        Floor(BaseFare + (Distance * PerDistanceRate))
    
    NotifyDrivers(Ride : ride_request):void=
        for (Driver : OnlineDrivers):
            Print("New ride request for {Driver}")
    
    ShowMainMenu(Player : player):void=
        Print("Showing Newber menu to {Player}")
    
    ShowRatingUI(Passenger : player, Driver : player):void=
        Print("Rate your driver {Driver}")

# Ride request structure
ride_request := class:
    var Passenger : player
    var Driver : ?player = false
    var Destination : vector3
    var Fare : int

GetPlayerLocation(Player : player):vector3=
    vector3{X := 0.0, Y := 0.0, Z := 0.0}

CalculateDistance(Loc1 : vector3, Loc2 : vector3):float=
    0.0
```

---

## 🏠 Property System (Verse)

### Property Manager

```verse
property_manager := class(creative_device):
    
    # Property ownership
    var PropertyOwners : [string]player = map{}
    var PropertyPrices : [string]int = map{}
    
    @editable
    EconomyManager : economy_manager = economy_manager{}
    
    Initialize():void=
        # Define property prices
        set PropertyPrices["Apartment_1"] = 5000
        set PropertyPrices["House_1"] = 15000
        set PropertyPrices["Villa_1"] = 50000
        
        Print("Property System - Initialized")
    
    # Purchase property
    PurchaseProperty(Player : player, PropertyID : string)<suspends>:bool=
        # Check if already owned
        if (Owner := PropertyOwners[PropertyID]):
            Print("Property already owned by {Owner}")
            return false
        
        # Check price
        if (Price := PropertyPrices[PropertyID]):
            # Check if player has money
            if (EconomyManager.HasMoney(Player, Price)):
                # Take money
                EconomyManager.TakeMoney(Player, Price).Await()
                
                # Transfer ownership
                set PropertyOwners[PropertyID] = Player
                
                # Give property key
                GivePropertyKey(Player, PropertyID)
                
                Print("{Player} purchased {PropertyID} for ${Price}")
                return true
        
        return false
    
    # Check if player owns property
    OwnsProperty(Player : player, PropertyID : string):bool=
        if (Owner := PropertyOwners[PropertyID]):
            return Owner = Player
        return false
    
    # Give property key
    GivePropertyKey(Player : player, PropertyID : string):void=
        # Grant access item/key
        Print("Giving property key to {Player} for {PropertyID}")
```

---

## 🚗 Vehicle System (Verse)

### Vehicle Manager

```verse
vehicle_manager := class(creative_device):
    
    # Vehicle ownership
    var VehicleOwners : [string]player = map{}
    var VehiclePrices : [string]int = map{}
    
    @editable
    EconomyManager : economy_manager = economy_manager{}
    
    # Vehicle spawners
    @editable
    CarSpawner : vehicle_spawner_device = vehicle_spawner_device{}
    
    Initialize():void=
        # Define vehicle prices
        set VehiclePrices["Sedan"] = 2000
        set VehiclePrices["Sports"] = 15000
        set VehiclePrices["SUV"] = 10000
        
        Print("Vehicle System - Initialized")
    
    # Purchase vehicle
    PurchaseVehicle(Player : player, VehicleType : string)<suspends>:bool=
        if (Price := VehiclePrices[VehicleType]):
            if (EconomyManager.HasMoney(Player, Price)):
                # Take money
                EconomyManager.TakeMoney(Player, Price).Await()
                
                # Generate unique vehicle ID
                VehicleID := "{Player}_{VehicleType}_{GetCurrentTime()}"
                
                # Register ownership
                set VehicleOwners[VehicleID] = Player
                
                # Spawn vehicle
                SpawnVehicle(Player, VehicleType)
                
                Print("{Player} purchased {VehicleType} for ${Price}")
                return true
        
        return false
    
    # Spawn player's vehicle
    SpawnVehicle(Player : player, VehicleType : string):void=
        # Use spawner to create vehicle
        CarSpawner.SpawnVehicle(agent[Player])
```

---

## 🌐 Multiplayer & Networking

### Network Replication

```verse
# Replicated player data
replicated_player_data := class<concrete>:
    @replicated
    var Money : int = 2000
    
    @replicated
    var JobTitle : string = "Unemployed"
    
    @replicated
    var Level : int = 1
    
    # Server authority
    SetMoney<localizes>(NewMoney : int):void=
        set Money = NewMoney
    
    SetJob<localizes>(NewJob : string):void=
        set JobTitle = NewJob
```

### Save/Load System

```verse
save_manager := class(creative_device):
    
    # Save player data
    SavePlayerData(Player : player, Data : player_data)<suspends>:void=
        # Convert to JSON and save to persistent storage
        Print("Saving data for {Player}")
        # Implementation depends on Epic's persistence API
    
    # Load player data
    LoadPlayerData(Player : player)<suspends>:?player_data=
        # Load from persistent storage
        Print("Loading data for {Player}")
        false  # Return loaded data or false if none exists
```

---

## 🎯 Performance Optimization

### Best Practices

1. **Use Object Pooling**:
```verse
vehicle_pool := class:
    var AvailableVehicles : []vehicle = array{}
    var ActiveVehicles : []vehicle = array{}
    
    GetVehicle():?vehicle=
        if (AvailableVehicles.Length > 0):
            Vehicle := AvailableVehicles[0]
            set AvailableVehicles = AvailableVehicles.RemoveAt(0)
            set ActiveVehicles += array{Vehicle}
            return Vehicle
        return false
    
    ReturnVehicle(Vehicle : vehicle):void=
        set ActiveVehicles = ActiveVehicles.RemoveElement(Vehicle)
        set AvailableVehicles += array{Vehicle}
```

2. **Limit Update Frequency**:
```verse
# Update every 0.5 seconds instead of every frame
OnBegin<override>()<suspends>:void=
    loop:
        Sleep(0.5)
        UpdatePlayerBalances()
```

3. **Use Spatial Queries**:
```verse
# Only update nearby players
GetNearbyPlayers(Location : vector3, Radius : float):[]player=
    AllPlayers := GetPlayspace().GetPlayers()
    NearbyPlayers := array{}
    
    for (Player : AllPlayers):
        PlayerLoc := GetPlayerLocation(Player)
        if (Distance(Location, PlayerLoc) < Radius):
            set NearbyPlayers += array{Player}
    
    NearbyPlayers

Distance(A : vector3, B : vector3):float=
    0.0  # Calculate Euclidean distance
```

---

## 📚 Additional Resources

### Learning Verse
- **Official Verse Documentation**: https://dev.epicgames.com/documentation/verse
- **UEFN Documentation**: https://dev.epicgames.com/documentation/uefn
- **Verse by Example**: Sample projects and tutorials
- **Epic Developer Community**: Forums and Discord

### Example Projects
1. Start with simple device interactions
2. Build a basic economy system
3. Add player progression
4. Implement multiplayer features

---

<div align="center">

**City of Legends - Unreal Engine Implementation**  
Version 1.0 | December 2025

*Professional Game Development with UEFN*

</div>
