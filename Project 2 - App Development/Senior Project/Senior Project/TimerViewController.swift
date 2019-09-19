//
//  TimerViewController.swift
//  Senior Project
//
//  Created by Connor Nelson on 5/28/19.
//  Copyright © 2019 Connor Nelson. All rights reserved.
//

import UIKit
import AVFoundation


class TimerViewController: UIViewController, UITextFieldDelegate {

    
    var audioPlayer: AVAudioPlayer?
    
    @IBOutlet weak var word1: UITextField!
    @IBOutlet weak var word2: UITextField!
    @IBOutlet weak var word3: UITextField!
    @IBOutlet weak var word4: UITextField!
    @IBOutlet weak var word5: UITextField!
    @IBOutlet weak var timerDisplay: UILabel!
    @IBOutlet weak var finalSoultion: UITextField!
    
    var check1 = false
    var check2 = false
    var check3 = false
    var check4 = false
    var check5 = false
    var timerGoing = true
    
    var counter = 0.0
    var timer = Timer()
    var minutes = 0
    
    func playSound(soundName : String){
        do {
            if let fileURL = Bundle.main.path(forResource: soundName, ofType: "mp3") {
                audioPlayer = try AVAudioPlayer(contentsOf: URL(fileURLWithPath: fileURL))
            } else {
                print("No file with specified name exists")
            }
        } catch let error {
            print("Can't play the audio file failed with an error \(error.localizedDescription)")
        }
        audioPlayer?.play()
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        playSound(soundName: "Beginning")
        word1.delegate = self
        word2.delegate = self
        word3.delegate = self
        word4.delegate = self
        word5.delegate = self
        timerDisplay.text = String(counter)
        timer = Timer.scheduledTimer(timeInterval: 0.1, target: self, selector: #selector(UpdateTimer), userInfo: nil, repeats: timerGoing)
        
    }
    
    @objc func UpdateTimer() {
        if (timerGoing){
            counter = counter + 0.1
            if counter >= 60{
                counter = 0
                minutes = minutes + 1
            }
            
            print(String(format: "%00.0f", minutes))
            print(counter)
            if minutes < 10{
                timerDisplay.text = "0" + String(minutes) + ":" + String(format: "%.1f", counter)
            }
            else{
                timerDisplay.text = String(minutes) + ":" + String(format: "%.1f", counter)
            }
        }
        

    }
    @IBAction func checkFinal(_ sender: Any) {
        if finalSoultion.text == "00000"{
            timerGoing = false
            finalSoultion.resignFirstResponder()
            
        }
        else{
            playSound(soundName: "incorrect")
        }
    }
    
    @IBAction func checkWord1(_ sender: Any) {
        if word1.text == "Whitaker" || word1.text == "whitaker" || word1.text == "Whitaker " || word1.text == "whitaker "{
            playSound(soundName: "correct")
            word1.resignFirstResponder()
            check1 = true
        }
        else{
            playSound(soundName: "incorrect")
        }
    }
    
    @IBAction func checkWord2(_ sender: Any) {
        if word2.text == "Stent" || word2.text == "Stent " || word2.text == "stent" || word2.text == "stent "{
            playSound(soundName: "correct")
            word2.resignFirstResponder()
            check2 = true
        }
        else{
            playSound(soundName: "incorrect")
        }
    }
    @IBAction func checkWord3(_ sender: Any) {
        if word3.text == "Martin" || word3.text == "Martin " || word3.text == "martin" || word3.text == "martin "{
            playSound(soundName: "correct")
            word3.resignFirstResponder()
            check3 = true
        }
        else{
            playSound(soundName: "incorrect")
        }
    }
    @IBAction func checkWord4(_ sender: Any) {
        if word4.text == "Wunderlich" || word4.text == "Wunderlich " || word4.text == "wunderlich" || word4.text == "wunderlich "{
            playSound(soundName: "correct")
            word4.resignFirstResponder()
            check4 = true
        }
        else{
            playSound(soundName: "incorrect")
        }
    }
    @IBAction func checkWord5(_ sender: Any) {
        if word5.text == "Spieker" || word5.text == "Spieker " || word5.text == "spieker" || word5.text == "spieker "{
            word5.resignFirstResponder()
            
            check5 = true
            if (check1 && check2 && check3 && check4 && check5){
                timerGoing = false
                playSound(soundName: "Ending")
            }
        }
        else{
            playSound(soundName: "incorrect")
        }
    }
    @IBAction func repeatInstructions(_ sender: Any) {
        playSound(soundName: "Beginning")
    }
    
    // UI TEXT FIELD DELEGATES
    
    func textFieldShouldReturn(_: UITextField) -> Bool{
        word1.resignFirstResponder()
        return true
    }
        // Do any additional setup after loading the view.
    }


    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */
    
    



