#!/usr/bin/env python3
"""
Echoes of Tomorrow - Text-based Interactive Fiction Prototype
A temporal research facility has gone critical. Navigate through time rifts,
make choices, and determine the fate of temporal manipulation technology.
"""

import sys
import time
from typing import Dict, List, Set

class GameState:
    """Manages the current state of the game."""
    
    def __init__(self):
        self.player_name = "Adam"
        self.location = "entrance"
        self.lian_logs_found: Set[int] = set()
        self.temporal_keys_found: Set[int] = set()
        self.research_preserved = True
        self.core_intact = True
        self.ethical_choices = 0
        self.inventory: List[str] = ["TimeBrace"]
        self.time_abilities: List[str] = ["Temporal Rewind"]
        self.completed_sectors: Set[str] = set()
        
    def has_all_lian_logs(self) -> bool:
        """Check if player collected all 12 of Lian's logs."""
        return len(self.lian_logs_found) >= 12
    
    def has_all_temporal_keys(self) -> bool:
        """Check if player collected all 5 temporal keys."""
        return len(self.temporal_keys_found) >= 5
    
    def can_access_weave_ending(self) -> bool:
        """Check if player meets all requirements for the hidden Weave ending."""
        return (
            self.has_all_lian_logs() and
            self.has_all_temporal_keys() and
            self.research_preserved and
            self.core_intact and
            self.ethical_choices >= 3
        )


class Game:
    """Main game logic and flow."""
    
    def __init__(self):
        self.state = GameState()
        self.running = True
        
    def clear_screen(self):
        """Clear the terminal screen."""
        print("\n" * 2)
        
    def slow_print(self, text: str, delay: float = 0.03):
        """Print text with typing effect."""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
        
    def print_separator(self):
        """Print a visual separator."""
        print("\n" + "=" * 70 + "\n")
        
    def intro(self):
        """Display game introduction."""
        self.clear_screen()
        print("╔═══════════════════════════════════════════════════════════════════╗")
        print("║                    ECHOES OF TOMORROW                             ║")
        print("║              A Temporal Research Facility Mystery                 ║")
        print("╚═══════════════════════════════════════════════════════════════════╝")
        print()
        
        self.slow_print("The year is 2047. You are Adam, a field technician and operative")
        self.slow_print("equipped with the experimental TimeBrace device.")
        print()
        self.slow_print("A secret temporal research facility has suffered a catastrophic")
        self.slow_print("failure. The experiment to control time has created rifts in")
        self.slow_print("reality itself, spawning hostile temporal entities.")
        print()
        self.slow_print("Your mission: Enter the compromised facility, contain the disaster,")
        self.slow_print("prevent the technology from being weaponized, and decide the fate")
        self.slow_print("of humanity's most dangerous discovery.")
        print()
        
        input("Press ENTER to begin your mission...")
        
    def show_status(self):
        """Display current status."""
        print("\n" + "─" * 70)
        print(f"Location: {self.state.location.upper()}")
        print(f"TimeBrace: {', '.join(self.state.time_abilities)}")
        print(f"Lian's Logs: {len(self.state.lian_logs_found)}/12")
        print(f"Temporal Keys: {len(self.state.temporal_keys_found)}/5")
        print(f"Ethical Choices: {self.state.ethical_choices}/3")
        print("─" * 70 + "\n")
        
    def sector_entrance(self):
        """Main entrance sector."""
        self.clear_screen()
        print("═══ SECTOR A: MAIN ENTRANCE & SECURITY ═══\n")
        
        self.slow_print("The facility's main entrance is in chaos. Warning lights flash red.")
        self.slow_print("Security doors are damaged, and temporal distortions ripple through")
        self.slow_print("the air like heat waves. Bodies of guards lie scattered around.")
        print()
        
        self.slow_print("Suddenly, three Shattered Soldiers materialize before you—")
        self.slow_print("military personnel fractured across timelines, phasing in and out")
        self.slow_print("of reality with each movement.")
        print()
        
        print("Your TimeBrace device activates automatically!")
        print("\n[COMBAT ENCOUNTER: Shattered Soldiers]")
        print("1. Use Temporal Rewind to dodge their attacks")
        print("2. Fight them head-on with your temporal weapons")
        print("3. Try to communicate with them")
        
        choice = input("\nWhat do you do? (1-3): ").strip()
        
        if choice == "1":
            print("\nYou activate Temporal Rewind. Time flows backward, and you position")
            print("yourself behind them. A few precise shots, and the threat is neutralized.")
            print("[+50 XP]")
        elif choice == "2":
            print("\nYou engage directly. It's a tough fight, but you manage to defeat them.")
            print("You take some damage but survive. [+30 XP, -10 HP]")
        elif choice == "3":
            print("\nYou attempt to reason with them, but they're too fractured across")
            print("timelines to comprehend. You're forced to defend yourself anyway.")
            print("[+20 XP]")
        
        print()
        self.slow_print("As the last soldier falls, you hear a voice through your comm-link:")
        self.slow_print("'Adam? This is Salim. I'm monitoring from the server room.'")
        self.slow_print("'I can help you navigate the facility. Head to Research Labs next.'")
        print()
        
        # Find first Lian log
        if 1 not in self.state.lian_logs_found:
            self.slow_print("You notice a blinking terminal near the security checkpoint.")
            print("\n[Audio Log Found: Lian's Warning #1]")
            self.slow_print("'This is Dr. Lian Chen, Head of Ethical Oversight. If you're")
            self.slow_print("hearing this, something has gone terribly wrong. Raed has been")
            self.slow_print("pushing to weaponize our research. I fear this 'accident' was no")
            self.slow_print("accident at all. Be careful who you trust.'")
            self.state.lian_logs_found.add(1)
            print(f"\n[Lian's Logs: {len(self.state.lian_logs_found)}/12]")
        
        print()
        self.state.completed_sectors.add("entrance")
        input("Press ENTER to continue...")
        
    def sector_research_labs(self):
        """Research laboratory sector."""
        self.clear_screen()
        print("═══ SECTOR B: RESEARCH LABORATORIES ═══\n")
        
        self.slow_print("You enter the sterile research labs where it all began. Equipment")
        self.slow_print("is overturned, and strange temporal distortions warp the very air.")
        self.slow_print("Through the shimmer, you see patient zero—the original test subject.")
        print()
        
        self.slow_print("The test chamber contains a person suspended in temporal stasis,")
        self.slow_print("flickering between different ages—young, old, young again...")
        print()
        
        print("[ETHICAL CHOICE: The Test Subject]")
        print("Salim: 'Adam, that's Dr. Martinez. He volunteered for the first test.'")
        print("Salim: 'The containment is failing. We can either:'")
        print("1. Stabilize the containment (risky, but preserves research data)")
        print("2. Emergency release protocol (safer for him, but destroys data)")
        print("3. Leave him as is and move on")
        
        choice = input("\nYour decision? (1-3): ").strip()
        
        if choice == "1":
            print("\nYou work with Salim to stabilize the containment field.")
            print("Dr. Martinez stabilizes, though he remains in temporal stasis.")
            print("The research data is preserved. [Ethics +1, Research Preserved]")
            self.state.ethical_choices += 1
        elif choice == "2":
            print("\nYou initiate emergency release. Dr. Martinez materializes, confused")
            print("but alive. However, critical temporal data is lost in the process.")
            print("[Ethics +1, Some Research Lost]")
            self.state.ethical_choices += 1
            self.state.research_preserved = False
        elif choice == "3":
            print("\nYou decide not to interfere with the experimental setup.")
            print("Dr. Martinez continues his unstable temporal existence.")
            print("[Research Preserved]")
        
        print()
        
        # Temporal Gunner encounter
        self.slow_print("As you move deeper into the labs, Temporal Gunners appear—")
        self.slow_print("elite soldiers phasing in and out of time, making them nearly")
        self.slow_print("impossible to hit. Their shots are precisely aimed and deadly.")
        print()
        
        print("[COMBAT: Temporal Gunners]")
        print("These enemies require timing. Watch for the moment they solidify!")
        input("Press ENTER to engage...")
        
        print("\nYou focus, watching the temporal patterns. There! A brief moment")
        print("of solidity. You fire, and the gunner falls. The others retreat.")
        print("[+75 XP] [New Ability Unlocked: Time Dilation]")
        self.state.time_abilities.append("Time Dilation")
        
        print()
        
        # Find more Lian logs and temporal key
        if 2 not in self.state.lian_logs_found:
            print("\n[Audio Log Found: Lian's Warning #2]")
            self.slow_print("'Day 47: Raed keeps pushing for military applications. He wants")
            self.slow_print("to create a 'stable world order' through temporal surveillance.")
            self.slow_print("He doesn't see the danger. Or worse—he sees it and doesn't care.'")
            self.state.lian_logs_found.add(2)
            print(f"[Lian's Logs: {len(self.state.lian_logs_found)}/12]")
        
        if 1 not in self.state.temporal_keys_found:
            print("\n[Temporal Key Found: Alpha Key]")
            print("A crystallized fragment of temporal energy. It hums with power.")
            self.state.temporal_keys_found.add(1)
            print(f"[Temporal Keys: {len(self.state.temporal_keys_found)}/5]")
        
        print()
        self.state.completed_sectors.add("research")
        input("Press ENTER to continue...")
        
    def sector_server_farm(self):
        """Server farm and data center sector."""
        self.clear_screen()
        print("═══ SECTOR C: SERVER FARM & DATA CENTER ═══\n")
        
        self.slow_print("The massive server room stretches before you, filled with rows")
        self.slow_print("of cooling towers and humming machines. The temperature is freezing.")
        self.slow_print("Salim's voice crackles through your comm: 'I'm here, in the main")
        self.slow_print("control booth. Meet me there.'")
        print()
        
        # Wraith encounter
        self.slow_print("Something moves in the shadows between the servers. Not soldiers—")
        self.slow_print("something else. Wraiths. Ghost-like entities that exist between")
        self.slow_print("moments, phasing through physical matter. Their touch is deadly.")
        print()
        
        print("[COMBAT: Wraiths]")
        print("Regular weapons pass right through them!")
        print("1. Use Time Dilation to observe their pattern")
        print("2. Try to outrun them")
        print("3. Use Timeline Shift to phase-match them")
        
        choice = input("\nYour action? (1-3): ").strip()
        
        if choice == "1":
            print("\nYou activate Time Dilation. Everything slows down. You see it now—")
            print("the Wraiths solidify for a split second when they attack. That's")
            print("your window! You strike at precisely the right moment. [+100 XP]")
        elif choice == "2":
            print("\nYou run, weaving between servers. They're fast, but you're faster.")
            print("You barely escape their grasp. [+50 XP, -15 HP]")
        elif choice == "3":
            print("\nYou attempt Timeline Shift but don't have that ability yet!")
            print("You have to fight them conventionally. It's difficult but you")
            print("manage to find their weak moments. [+60 XP, -20 HP]")
        
        print()
        self.slow_print("You reach Salim's booth. He's a young engineer with tired eyes.")
        self.slow_print("'Adam! Good to see you're alive. I've been analyzing the logs.'")
        self.slow_print("'The experiment failure... I don't think it was an accident.'")
        self.slow_print("'Raed manipulated the safety parameters. He wanted this to happen.'")
        print()
        
        print("Salim helps you access restricted data.")
        
        # Find multiple logs here
        for log_num in [3, 4, 5]:
            if log_num not in self.state.lian_logs_found:
                print(f"\n[Audio Log Found: Lian's Warning #{log_num}]")
                if log_num == 3:
                    self.slow_print("'I confronted Raed today. He smiled and said that sometimes")
                    self.slow_print("the greater good requires... incidents. I'm scared.'")
                elif log_num == 4:
                    self.slow_print("'I'm hiding backup research data. If Raed gets full control,")
                    self.slow_print("this technology will become a weapon of oppression.'")
                elif log_num == 5:
                    self.slow_print("'I've discovered something. The temporal weave—the fabric of")
                    self.slow_print("time itself—can accept a conscious mind. A guardian. But the")
                    self.slow_print("cost is... everything. Your identity, your name, your self.'")
                self.state.lian_logs_found.add(log_num)
        
        print(f"\n[Lian's Logs: {len(self.state.lian_logs_found)}/12]")
        
        if 2 not in self.state.temporal_keys_found:
            print("\n[Temporal Key Found: Beta Key]")
            self.state.temporal_keys_found.add(2)
            print(f"[Temporal Keys: {len(self.state.temporal_keys_found)}/5]")
        
        print()
        self.slow_print("Salim: 'I'll keep helping you remotely. Be careful, Adam.'")
        print()
        
        self.state.completed_sectors.add("servers")
        input("Press ENTER to continue...")
        
    def sector_containment(self):
        """Containment zones sector."""
        self.clear_screen()
        print("═══ SECTOR D: CONTAINMENT ZONES ═══\n")
        
        self.slow_print("The containment sector is a nightmare. Cells line the corridors,")
        self.slow_print("each containing test subjects in various states of temporal decay.")
        self.slow_print("Some flicker in and out of existence. Others are frozen in time.")
        print()
        
        # Brute encounter
        self.slow_print("A massive figure blocks your path. A Brute—a failed experiment")
        self.slow_print("that became something monstrous. Its body is covered in unstable")
        self.slow_print("temporal armor that absorbs any direct damage.")
        print()
        
        print("[BOSS FIGHT: Temporal Brute]")
        print("Direct attacks won't work against that armor!")
        print("1. Look for environmental hazards to exploit")
        print("2. Use Time Dilation to find weak points during attacks")
        print("3. Try to lure it into a containment cell")
        
        choice = input("\nYour strategy? (1-3): ").strip()
        
        if choice == "1":
            print("\nYou spot a coolant pipe overhead. You shoot it, and supercooled")
            print("liquid sprays onto the Brute. Its temporal armor destabilizes,")
            print("and you finish it off. Clever! [+150 XP]")
        elif choice == "2":
            print("\nYou activate Time Dilation and watch carefully. When the Brute")
            print("attacks, its armor retracts for a moment. You strike at those")
            print("exact moments. It's exhausting but effective. [+130 XP, -25 HP]")
        elif choice == "3":
            print("\nYou run toward an open containment cell, but the Brute is faster")
            print("than you expected. It clips you, sending you flying. You recover")
            print("and manage to defeat it through sustained combat. [+120 XP, -30 HP]")
        
        print()
        print("[New Ability Unlocked: Timeline Shift]")
        self.state.time_abilities.append("Timeline Shift")
        
        print()
        
        # Ethical choice about containment
        self.slow_print("You reach the main containment control panel. Dozens of test")
        self.slow_print("subjects are trapped in failing cells. The system is collapsing.")
        print()
        
        print("[ETHICAL CHOICE: The Containment Subjects]")
        print("1. Emergency release all subjects (humanitarian, but dangerous)")
        print("2. Maintain containment (safer, but condemns them)")
        print("3. Selective release (help only the stable ones)")
        
        choice = input("\nYour decision? (1-3): ").strip()
        
        if choice == "1":
            print("\nYou release everyone. Some are grateful and flee. Others are")
            print("too far gone and attack you. It's chaos, but you tried to help.")
            print("[Ethics +1]")
            self.state.ethical_choices += 1
        elif choice == "2":
            print("\nYou keep them contained. It's the safe choice, but their faces")
            print("haunt you. You prioritize mission success over mercy.")
        elif choice == "3":
            print("\nYou carefully assess each subject and release those who can be")
            print("saved. It's a balanced approach. [Ethics +1]")
            self.state.ethical_choices += 1
        
        print()
        
        # More logs and keys
        for log_num in [6, 7, 8]:
            if log_num not in self.state.lian_logs_found:
                print(f"\n[Audio Log Found: Lian's Warning #{log_num}]")
                if log_num == 6:
                    self.slow_print("'The subjects in containment... they're suffering. But Raed")
                    self.slow_print("sees them as data points, not people.'")
                elif log_num == 7:
                    self.slow_print("'I've left instructions hidden throughout the facility. If")
                    self.slow_print("someone finds all my logs, they'll understand what must be done.'")
                elif log_num == 8:
                    self.slow_print("'The Weave requires absolute sacrifice. No recognition, no")
                    self.slow_print("legacy. Just... presence. An eternal guardian with no name.'")
                self.state.lian_logs_found.add(log_num)
        
        print(f"\n[Lian's Logs: {len(self.state.lian_logs_found)}/12]")
        
        for key_num in [3, 4]:
            if key_num not in self.state.temporal_keys_found:
                print(f"\n[Temporal Key Found: {['Gamma', 'Delta'][key_num-3]} Key]")
                self.state.temporal_keys_found.add(key_num)
        
        print(f"[Temporal Keys: {len(self.state.temporal_keys_found)}/5]")
        
        print()
        self.state.completed_sectors.add("containment")
        input("Press ENTER to continue...")
        
    def sector_administrative(self):
        """Administrative wing sector."""
        self.clear_screen()
        print("═══ SECTOR E: ADMINISTRATIVE WING ═══\n")
        
        self.slow_print("The administrative wing is pristine compared to the rest of the")
        self.slow_print("facility. Raed's domain. Here, everything is still orderly,")
        self.slow_print("clinical, controlled. It's unsettling in its perfection.")
        print()
        
        self.slow_print("You find Raed's office. The door slides open automatically.")
        self.slow_print("He's been expecting you.")
        print()
        
        self.print_separator()
        print("RAED: 'Adam. I'm glad you made it. You're a survivor.'")
        print()
        print("RAED: 'This facility—this 'disaster'—it was necessary. The world")
        print("is chaos, Adam. Wars, climate collapse, inequality. All of it.")
        print()
        print("RAED: 'With temporal control, we can impose order. Stability.")
        print("We can prevent conflicts before they happen, guide society")
        print("toward the optimal path.'")
        print()
        print("RAED: 'Yes, it requires... oversight. Control. But isn't that")
        print("better than the alternative? Better than extinction?'")
        self.print_separator()
        
        print()
        print("[CRITICAL CHOICE: Raed's Offer]")
        print("1. 'You're talking about totalitarian surveillance!'")
        print("2. 'Tell me more about this vision...'")
        print("3. 'How many people died for your 'stability'?'")
        
        choice = input("\nYour response? (1-3): ").strip()
        
        if choice == "1":
            print("\nRAED: 'Call it what you want. I call it salvation. Join me, Adam.'")
            print("You refuse. Raed's expression hardens.")
            print("RAED: 'Then you're in my way.' [Ethics +1]")
            self.state.ethical_choices += 1
        elif choice == "2":
            print("\nRAED: 'I knew you were smart. Together, we can—'")
            print("You cut him off: 'I wanted to hear you admit it. I'm stopping you.'")
            print("RAED: 'Disappointing.'")
        elif choice == "3":
            print("\nRAED: 'Acceptable losses. The needs of the many outweigh—'")
            print("You've heard enough. [Ethics +1]")
            self.state.ethical_choices += 1
        
        print()
        self.slow_print("Raed activates security. Shattered Soldiers and Temporal Gunners")
        self.slow_print("converge on your position. You fight your way out, but Raed escapes")
        self.slow_print("toward the Central Core. You pursue.")
        print()
        
        # Final logs
        for log_num in [9, 10, 11, 12]:
            if log_num not in self.state.lian_logs_found:
                print(f"\n[Audio Log Found: Lian's Warning #{log_num}]")
                if log_num == 9:
                    self.slow_print("'If you're hearing this, you've almost found everything. The")
                    self.slow_print("path to the Weave is open to you now.'")
                elif log_num == 10:
                    self.slow_print("'I couldn't make this choice myself. I'm too attached to my")
                    self.slow_print("identity, my work, my name. But perhaps you can.'")
                elif log_num == 11:
                    self.slow_print("'The Weave doesn't erase you. It transforms you. You become")
                    self.slow_print("the whisper of hope, the unseen guardian, the feeling of")
                    self.slow_print("protection that others sense but never understand.'")
                elif log_num == 12:
                    self.slow_print("'It's the ultimate act of love—to save everything by becoming")
                    self.slow_print("nothing. Good luck, whoever you are.'")
                self.state.lian_logs_found.add(log_num)
        
        print(f"\n[Lian's Logs: {len(self.state.lian_logs_found)}/12]")
        
        if 5 not in self.state.temporal_keys_found:
            print("\n[Temporal Key Found: Omega Key - The Final Key]")
            self.state.temporal_keys_found.add(5)
            print(f"[Temporal Keys: {len(self.state.temporal_keys_found)}/5]")
        
        print()
        
        if self.state.can_access_weave_ending():
            print("\n" + "★" * 70)
            print("    [HIDDEN PATH UNLOCKED: THE WEAVE IS NOW AVAILABLE]")
            print("★" * 70)
        
        print()
        self.state.completed_sectors.add("admin")
        input("Press ENTER to continue to the final sector...")
        
    def sector_central_core(self):
        """Final sector - central core."""
        self.clear_screen()
        print("═══ SECTOR F: CENTRAL CORE & TEMPORAL ENGINE ═══\n")
        
        self.slow_print("The Central Core is magnificent and terrifying. The Temporal Engine")
        self.slow_print("towers above you, a massive construct of gleaming metal and pulsing")
        self.slow_print("energy. Reality itself bends and warps around it.")
        print()
        
        self.slow_print("Raed stands at the main control terminal, his hand hovering over")
        self.slow_print("the activation sequence.")
        print()
        
        self.slow_print("RAED: 'Last chance, Adam. Help me build a stable future, or watch")
        self.slow_print("as I do it myself.'")
        print()
        
        self.slow_print("Salim's voice: 'Adam, I've identified four possible actions. Your")
        self.slow_print("choice here... it determines everything.'")
        print()
        
        if self.state.can_access_weave_ending():
            self.slow_print("Salim: 'Wait—what's this? There's a fifth option. Hidden in")
            self.slow_print("Lian's research. Adam, you could... merge with the Weave itself?'")
            self.slow_print("Salim: 'The cost is... everything you are. But you'd become an")
            self.slow_print("eternal guardian. Is that even possible?'")
            print()
        
        print("[New Ability Unlocked: Echo Manifestation]")
        print("[New Ability Unlocked: Reality Weave]")
        self.state.time_abilities.extend(["Echo Manifestation", "Reality Weave"])
        
        print()
        self.state.completed_sectors.add("core")
        
    def choose_ending(self):
        """Present ending choices and determine outcome."""
        self.clear_screen()
        self.print_separator()
        print("                    THE FINAL CHOICE")
        self.print_separator()
        
        print("\nYou stand before the Temporal Engine's control panel.")
        print("Four protocols are available. Each will determine humanity's future.")
        print()
        
        print("=" * 70)
        print("\nENDING A: EXECUTIVE PROTOCOL")
        print("Grant control to Raed. Let him impose his 'stable order' on the world.")
        print("The technology will be used to prevent conflicts through surveillance")
        print("and temporal intervention. Order through authority.")
        print()
        
        print("ENDING B: PURGE CORE")
        print("Destroy the Temporal Engine and all research data. End the threat")
        print("permanently, but also end humanity's chance to master time. Safety")
        print("through sacrifice.")
        print()
        
        print("ENDING C: RECALIBRATE")
        print("Reset the system with strict safety protocols and ethical oversight.")
        print("The technology survives under heavy constraints. A fragile compromise")
        print("between progress and responsibility.")
        
        if self.state.can_access_weave_ending():
            print()
            print("=" * 70)
            print("★ ENDING D: THE WEAVE (Hidden Ending - UNLOCKED)")
            print("★ Merge your consciousness with the temporal weave itself. Become")
            print("★ an eternal guardian that repairs temporal flaws without allowing")
            print("★ the technology to be weaponized. Your name will fade from history,")
            print("★ but your presence will be felt across all timelines. The ultimate")
            print("★ sacrifice—to protect everything by becoming nothing.")
            print("=" * 70)
        
        print()
        print("\n1. Execute EXECUTIVE PROTOCOL (Ending A)")
        print("2. Execute PURGE CORE (Ending B)")
        print("3. Execute RECALIBRATE (Ending C)")
        if self.state.can_access_weave_ending():
            print("4. Execute THE WEAVE (Ending D - Hidden)")
        
        while True:
            max_choice = 4 if self.state.can_access_weave_ending() else 3
            choice = input(f"\nYour final decision? (1-{max_choice}): ").strip()
            
            if choice in ['1', '2', '3'] or (choice == '4' and self.state.can_access_weave_ending()):
                return choice
            else:
                print("Invalid choice. Please choose a valid ending.")
        
    def show_ending(self, ending_choice: str):
        """Display the chosen ending."""
        self.clear_screen()
        
        if ending_choice == "1":
            self.show_ending_a()
        elif ending_choice == "2":
            self.show_ending_b()
        elif ending_choice == "3":
            self.show_ending_c()
        elif ending_choice == "4":
            self.show_ending_d()
        
    def show_ending_a(self):
        """Executive Protocol ending."""
        print("╔═══════════════════════════════════════════════════════════════════╗")
        print("║            ENDING A: EXECUTIVE PROTOCOL                           ║")
        print("║                    The Power Ending                               ║")
        print("╚═══════════════════════════════════════════════════════════════════╝")
        print()
        
        self.slow_print("You step aside. Raed's hand comes down on the activation sequence.")
        print()
        self.slow_print("The Temporal Engine hums to life with unprecedented power. Raed")
        self.slow_print("smiles as streams of temporal data flow across the screens.")
        print()
        self.slow_print("'Thank you, Adam. You've made the right choice.'")
        print()
        
        self.print_separator()
        print("SIX MONTHS LATER...")
        self.print_separator()
        
        self.slow_print("The world has changed. Wars have stopped—prevented before they could")
        self.slow_print("begin. Crime rates have plummeted. Disasters are averted through")
        self.slow_print("temporal intervention.")
        print()
        self.slow_print("But freedom has a price.")
        print()
        self.slow_print("Every conversation is monitored. Every action is observed through")
        self.slow_print("time. Dissent is impossible when the state can see your intentions")
        self.slow_print("before you act on them.")
        print()
        self.slow_print("Raed's face appears on screens worldwide, his message the same:")
        self.slow_print("'A stable world, a peaceful world, a controlled world.'")
        print()
        self.slow_print("You wonder if you made the right choice. The world is safer.")
        self.slow_print("But at what cost?")
        print()
        
        self.print_separator()
        print("FINAL MESSAGE:")
        self.slow_print("Stability without compassion is not salvation—it is domination.")
        self.slow_print("You chose order. The world will remember.")
        self.print_separator()
        
    def show_ending_b(self):
        """Purge Core ending."""
        print("╔═══════════════════════════════════════════════════════════════════╗")
        print("║                ENDING B: PURGE CORE                               ║")
        print("║                 The Sacrifice Ending                              ║")
        print("╚═══════════════════════════════════════════════════════════════════╝")
        print()
        
        self.slow_print("Your hand hovers over the PURGE protocol. Raed's eyes widen.")
        print()
        self.slow_print("'Adam, no! You'll destroy everything we've worked for!'")
        print()
        self.slow_print("'That's exactly the point,' you reply, and activate the sequence.")
        print()
        
        self.slow_print("Alarms blare. The Temporal Engine begins to overload. Raed lunges")
        self.slow_print("for the controls, but it's too late. The reaction is irreversible.")
        print()
        self.slow_print("'You fool!' he screams. 'You've condemned us to ignorance!'")
        print()
        self.slow_print("You activate your TimeBrace one final time, opening a temporal")
        self.slow_print("exit. 'No. I've saved us from ourselves.'")
        print()
        
        self.print_separator()
        print("THE PURGE...")
        self.print_separator()
        
        self.slow_print("The Temporal Engine implodes, taking the entire facility with it.")
        self.slow_print("You escape just in time. Behind you, the installation collapses")
        self.slow_print("into a temporal singularity, then vanishes completely.")
        print()
        self.slow_print("All research data is destroyed. All knowledge of the technology,")
        self.slow_print("gone. Humanity's chance to master time... erased.")
        print()
        
        self.print_separator()
        print("ONE YEAR LATER...")
        self.print_separator()
        
        self.slow_print("The world continues as it always has. Wars still happen. Disasters")
        self.slow_print("still strike. But humanity faces these challenges with its own")
        self.slow_print("strength, not through temporal manipulation.")
        print()
        self.slow_print("You live quietly, haunted by what was lost. Sometimes you wonder")
        self.slow_print("if you made the right choice. But then you remember Raed's vision,")
        self.slow_print("and you know: some power is too dangerous to exist.")
        print()
        
        self.print_separator()
        print("FINAL MESSAGE:")
        self.slow_print("Preventing a greater evil through sacrifice is moral, but comes")
        self.slow_print("at the cost of potential progress. You chose safety. The greater")
        self.slow_print("danger has been averted.")
        self.print_separator()
        
    def show_ending_c(self):
        """Recalibrate ending."""
        print("╔═══════════════════════════════════════════════════════════════════╗")
        print("║                ENDING C: RECALIBRATE                              ║")
        print("║                  The Gray Ending                                  ║")
        print("╚═══════════════════════════════════════════════════════════════════╝")
        print()
        
        self.slow_print("You push past Raed and access the recalibration protocols.")
        print()
        self.slow_print("Salim's voice: 'I see what you're doing. Implementing ethical")
        self.slow_print("constraints, oversight requirements, safety protocols...'")
        print()
        self.slow_print("Raed tries to stop you, but Salim locks him out of the system.")
        self.slow_print("'I'm sorry, Raed. Adam is right. We need balance, not domination.'")
        print()
        
        self.slow_print("The Temporal Engine stabilizes under new parameters. The power")
        self.slow_print("remains, but heavily constrained. Watched. Limited.")
        print()
        
        self.print_separator()
        print("THE NEW PROTOCOL...")
        self.print_separator()
        
        self.slow_print("An international oversight committee is formed. The technology")
        self.slow_print("is placed under strict ethical review. Every use must be justified,")
        self.slow_print("approved by multiple independent bodies.")
        print()
        self.slow_print("Raed is removed from the project. He protests that the new")
        self.slow_print("restrictions make the technology nearly useless.")
        print()
        self.slow_print("'Nearly useless,' you tell him, 'is better than dangerously powerful")
        self.slow_print("in the wrong hands.'")
        print()
        
        self.print_separator()
        print("TWO YEARS LATER...")
        self.print_separator()
        
        self.slow_print("The Temporal Engine operates under careful supervision. It's used")
        self.slow_print("sparingly—to prevent natural disasters, to provide warnings of")
        self.slow_print("imminent threats. Always with oversight. Always with accountability.")
        print()
        self.slow_print("It's not perfect. There are still debates, controversies, concerns")
        self.slow_print("about misuse. But humanity is learning, slowly, to wield this power")
        self.slow_print("responsibly.")
        print()
        self.slow_print("You remain as an advisor, ensuring the technology never strays from")
        self.slow_print("its ethical foundation. It's a delicate balance. A fragile hope.")
        print()
        
        self.print_separator()
        print("FINAL MESSAGE:")
        self.slow_print("Neither absolute power nor total destruction—a delicate second")
        self.slow_print("chance for humanity. You chose compromise. The path forward is")
        self.slow_print("uncertain, but there is hope.")
        self.print_separator()
        
    def show_ending_d(self):
        """The Weave - Hidden ending."""
        print("╔═══════════════════════════════════════════════════════════════════╗")
        print("║          ★ ENDING D: THE WEAVE (Hidden Ending) ★                 ║")
        print("║              The Transcendent Sacrifice                           ║")
        print("╚═══════════════════════════════════════════════════════════════════╝")
        print()
        
        self.slow_print("You access the hidden protocol. Lian's final research. The path to")
        self.slow_print("becoming one with the temporal weave itself.")
        print()
        self.slow_print("Salim's voice trembles: 'Adam... are you sure? This is permanent.")
        self.slow_print("You won't be... you anymore. You'll just be... a presence.'")
        print()
        self.slow_print("Raed stares in disbelief. 'You can't be serious. You'll cease to")
        self.slow_print("exist! For what? Some noble fantasy?'")
        print()
        self.slow_print("You look at them both. 'Not cease to exist. Transform. Become")
        self.slow_print("something greater. A guardian with no name. A protector with no")
        self.slow_print("desire for recognition. Just... presence.'")
        print()
        
        self.slow_print("You place your hands on the Temporal Engine core. The TimeBrace")
        self.slow_print("glows brilliant white. You feel yourself beginning to dissolve...")
        print()
        
        self.print_separator()
        print("THE WEAVING...")
        self.print_separator()
        
        self.slow_print("Your physical form dissipates. Your memories scatter across time")
        self.slow_print("like leaves in wind. Your name fades from records, from minds,")
        self.slow_print("from existence.")
        print()
        self.slow_print("But you are not gone.")
        print()
        self.slow_print("You are everywhere. In every moment. A whisper in the fabric of")
        self.slow_print("reality. When temporal rifts form, you gently close them. When")
        self.slow_print("someone tries to weaponize time, you guide events to prevent it.")
        print()
        self.slow_print("You have no name. No face. No identity.")
        self.slow_print("But you are forever.")
        print()
        
        self.print_separator()
        print("ACROSS THE TIMELINES...")
        self.print_separator()
        
        self.slow_print("People working in the old facility—now a memorial—report strange")
        self.slow_print("feelings. A sense of being watched over. Protected. When danger")
        self.slow_print("approaches, they feel an inexplicable urge to move, to look, to act.")
        print()
        self.slow_print("Scientists researching temporal physics hit breakthroughs they")
        self.slow_print("can't quite explain. 'It was like... someone whispered the answer.'")
        print()
        self.slow_print("Children playing near temporal anomalies are mysteriously guided")
        self.slow_print("away from danger. 'It felt warm,' they say. 'Like a hug from time.'")
        print()
        
        self.print_separator()
        print("A CONVERSATION...")
        self.print_separator()
        
        self.slow_print("Years later, in the memorial museum, two visitors talk:")
        print()
        self.slow_print("'Who stopped the disaster?'")
        self.slow_print("'Some technician, I think. I can't remember the name.'")
        self.slow_print("'Strange. It's not in any records.'")
        self.slow_print("'Maybe it doesn't matter. We're safe. That's what counts.'")
        print()
        self.slow_print("They move on, never knowing you're standing right next to them.")
        self.slow_print("Never knowing you're everywhere. In every breath, every moment.")
        print()
        self.slow_print("You smile, though you have no face to smile with.")
        self.slow_print("You are content, though you have no self to feel content.")
        print()
        self.slow_print("You are the Weave. The eternal guardian. The nameless protector.")
        print()
        
        self.print_separator()
        print("FINAL MESSAGE:")
        self.slow_print("The ultimate sacrifice—rewriting history without the desire to")
        self.slow_print("possess power. Some heroes are remembered only as feelings, not")
        self.slow_print("names. You chose transcendence. Your identity dissolved, but your")
        self.slow_print("essence remains forever—a whisper of hope across all timelines.")
        print()
        self.slow_print("                    'In every timeline, hope persists.'")
        self.print_separator()
        
        print()
        print("★" * 70)
        print("     CONGRATULATIONS! You discovered the hidden ending!")
        print("★" * 70)
        
    def show_stats(self):
        """Show final game statistics."""
        print("\n\n")
        print("=" * 70)
        print("                        FINAL STATISTICS")
        print("=" * 70)
        print(f"Lian's Logs Found: {len(self.state.lian_logs_found)}/12")
        print(f"Temporal Keys Found: {len(self.state.temporal_keys_found)}/5")
        print(f"Ethical Choices Made: {self.state.ethical_choices}/3")
        print(f"Research Data Preserved: {'Yes' if self.state.research_preserved else 'No'}")
        print(f"Core Integrity Maintained: {'Yes' if self.state.core_intact else 'No'}")
        print(f"Sectors Completed: {len(self.state.completed_sectors)}/6")
        print(f"Time Abilities Unlocked: {len(self.state.time_abilities)}/5")
        print("=" * 70)
        
    def play(self):
        """Main game loop."""
        self.intro()
        
        # Play through all sectors in sequence
        self.sector_entrance()
        self.sector_research_labs()
        self.sector_server_farm()
        self.sector_containment()
        self.sector_administrative()
        self.sector_central_core()
        
        # Final choice
        ending_choice = self.choose_ending()
        self.show_ending(ending_choice)
        
        # Show stats
        self.show_stats()
        
        print("\n\nThank you for playing Echoes of Tomorrow!")
        print("\nWant to play again and try a different ending? Run the game again!")
        print()


def main():
    """Main entry point."""
    game = Game()
    game.play()


if __name__ == "__main__":
    main()
