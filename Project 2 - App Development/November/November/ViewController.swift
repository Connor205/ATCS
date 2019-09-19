//
//  ViewController.swift
//  November
//
//  Created by Connor Nelson on 1/9/19.
//  Copyright © 2019 Connor Nelson. All rights reserved.
//

import UIKit

protocol ViewControllerDelegate: class {
    func getScore (_ controller: HighscoreViewController, score: Int)
}

class ViewController: UIViewController, HighscoreVCDelegate {

    weak var delegate: ViewControllerDelegate?
    var scoresArray: [Int] = []
    
    var currentValue: Int = 0
    var targetValue: Int = 0
    var score: Int = 0
    var round: Int = 0
    
    
    
    @IBOutlet weak var slider: UISlider!
    @IBOutlet weak var targetLabel: UILabel!
    @IBOutlet weak var scoreLabel: UILabel!
    @IBOutlet weak var roundLabel: UILabel!
    override func viewDidLoad() {
        
        super.viewDidLoad()
        let thumbImageNormal = UIImage(named: "SliderThumb-Normal")
        slider.setThumbImage(thumbImageNormal, for: .normal)
        let thumbImageHighlighted = UIImage(named:"SliderThumb-Highlighted")
        slider.setThumbImage(thumbImageHighlighted, for: .highlighted)
        
        startOver()
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    func updateLabels()
    {
        targetLabel.text = String(targetValue)
        roundLabel.text = String(round)
        scoreLabel.text = String(score)
    }
    
    @IBAction func showAlert()
    {
        if round < 2
        {
            let difference = abs(currentValue - targetValue)
            var points = 100 - difference * difference
            if difference == 0
            {
                points += 100
            }
            score += points
            scoreLabel.text = String(score)
            let myMessage = "The value of the slider is now: \(lroundf(slider.value))\n" + "The target number is: \(targetValue)\n" + "You Scored \(points)"
            let alert = UIAlertController(title: "Round Score", message: myMessage, preferredStyle: .alert)
            let action = UIAlertAction(title: "OK", style: .default, handler: { _ in self.newRound()})
            alert.addAction(action)
            present(alert, animated: true, completion: nil)
        }
        else{
            let difference = abs(currentValue - targetValue)
            var points = 100 - difference * difference
            if difference == 0
            {
                points += 100
            }
            score += points
            scoreLabel.text = String(score)
            performSegue(withIdentifier: "toHighscore", sender: self)
        }
        
    }
    @IBAction func showInstructions()
    {
        let myMessage = "Move the slider to the point on the line that corresponds to the target value. Then click hit me to receive your score. You may click the restart button to restart"
        let alert = UIAlertController(title: "Instructions", message: myMessage, preferredStyle: .alert)
        let action = UIAlertAction(title: "OK", style: .default, handler: { _ in self.newRound()})
        alert.addAction(action)
        present(alert, animated: true, completion: nil)
    }
    
    @IBAction func sliderMoved ( _ slider:UISlider)
    {
        currentValue = lroundf(slider.value)
    }
    
    func newRound ()
    {
        targetValue = Int.random(in: 1...100)
        currentValue = 50
        slider.value = 50
        round += 1
        updateLabels()
    }
    
    @IBAction func startOver()
    {
        score = 0
        scoreLabel.text = String(score)
        round = 0
        newRound()
    }
    
    func displayScore(_ controller: HighscoreViewController, score: Int) {
        
    }
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "toHighscore"
        {
            let controller = segue.destination as! HighscoreViewController
            controller.delegate = self
            controller.score = score
            controller.scoresArray = scoresArray
            
        }
    }

}

