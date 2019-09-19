//
//  HighscoreViewController.swift
//  November
//
//  Created by Connor Nelson on 2/14/19.
//  Copyright © 2019 Connor Nelson. All rights reserved.
//

import UIKit

protocol HighscoreVCDelegate: class {
    func displayScore(_ controller: HighscoreViewController, score: Int)
}

class HighscoreViewController: UIViewController, ViewControllerDelegate {
    func getScore(_ controller: HighscoreViewController, score: Int) {
    }
    
    @IBOutlet weak var SecondScoreLabel: UILabel!
    @IBOutlet weak var lastScore: UILabel!
    @IBOutlet weak var highscoreLabel: UILabel!
    @IBOutlet weak var ThirdScoreLabel: UILabel!
    var highscore: Int = 0
    var scoresArray: [Int] = []
    
    weak var delegate: HighscoreVCDelegate?
    var score : Int?

    override func viewDidLoad() {
        super.viewDidLoad()
        if score != nil{
            scoresArray.append(score!)
            scoresArray.sort()
            print(scoresArray)
            lastScore.text = String(score!)
        }
        else{
            lastScore.text = "NA"
        }
        if scoresArray.count >= 3{
            highscoreLabel.text = String(scoresArray.last!)
            SecondScoreLabel.text = String(scoresArray[scoresArray.count-2])
            ThirdScoreLabel.text = String(scoresArray[scoresArray.count - 3])
        }
        else if scoresArray.count == 2{
            highscoreLabel.text = String(scoresArray.last!)
            SecondScoreLabel.text = String(scoresArray[scoresArray.count-2])
        }
        else if scoresArray.count == 1{
            highscoreLabel.text = String(scoresArray.last!)
        }
    }
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "playAgain"
        {
            let controller = segue.destination as! ViewController
            controller.delegate = self
            controller.scoresArray = scoresArray
        }
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


