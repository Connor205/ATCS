//
//  HandChoosingVC.swift
//  ATCS Final Project
//
//  Created by Connor Nelson on 3/19/19.
//  Copyright © 2019 Connor Nelson. All rights reserved.
//

import UIKit

class HandChoosingVC: UIViewController {
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier != "restart"{
            if segue.identifier == "addCard" {
                let CardSelectionViewController = segue.destination as! CardSelectionViewController
            }
            else{
                let ResultsViewController = segue.destination as! ResultsViewController
                ResultsViewController.board = board
                ResultsViewController.hand = hand
                if segue.identifier == "Flush"{
                    ResultsViewController.attempting = "Flush"
                }
            }


            
            }
        }
    
    var hand: [card] = []
    var board: [card] = []
    
    @IBOutlet weak var straightLabel: UILabel!
    @IBOutlet weak var flushLabel: UILabel!
    @IBOutlet weak var pairLabel: UILabel!
    @IBOutlet weak var twopairLabel: UILabel!
    @IBOutlet weak var setlabel: UILabel!
    @IBOutlet weak var straightflushLabel: UILabel!
    override func viewDidLoad() {
        super.viewDidLoad()
        var percents = ["Straight": 0.0,
                        "Flush": 0.0,
                        "Pair": 0.0,
                        "TwoPair": 0.0,
                        "Set": 0.0,
                        "StraightFlush": 0.0]
        
        var suitCounts = ["Hearts": 0,
                          "Spades": 0,
                          "Diamonds": 0,
                          "Clubs": 0]
        var totalMaxSuit = 0

        for i in hand{
            suitCounts[i.suit] = suitCounts[i.suit]! + 1
        }
        for i in board{
            suitCounts[i.suit] = suitCounts[i.suit]! + 1
        }
        for (suit, number) in suitCounts{
            if number > totalMaxSuit{
                totalMaxSuit = number
            }
        }
        
        var valueCounts = ["Ace": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "Ten": 0, "Jack": 0, "Queen": 0, "King": 0]
        for i in hand{
            valueCounts[i.value] = valueCounts[i.value]! + 1
        }
        for i in board{
            valueCounts[i.value] = valueCounts[i.value]! + 1
        }
        var numPairs = 0
        var totalMaxValue = 0
        for (value, number) in valueCounts{
            if number > totalMaxValue{
                totalMaxValue = number
            }
        }
        for (value, number)  in valueCounts{
            if number >= 2{
                numPairs = numPairs + 1
            }
        }
        
        // NO CARDS ON BOARD
        if board.count == 0 && hand.count == 2{
            if totalMaxSuit == 2{
                percents["Flush"] = 23.59
            }
            else{
                percents["Flush"] = 3.4
            }
            if totalMaxValue == 2{
                percents["Pair"] = 100
                percents["Set"] = 12.5
                percents["Straight"] = 1.1
            }
            else{
                percents["Pair"] = 33.35
                percents["Set"] = 4.8
                percents["Straight"] = 3.3
            }
            if numPairs >= 2{
                percents["TwoPair"] = 100
            }
            else {
                percents["TwoPair"] = 11.1
            }
            percents["StraightFlush"] = 100 * (0.01 * percents["Flush"]! * 0.01 * percents["Straight"]!)
        }
        else if board.count == 3{
            //Flush
            if totalMaxSuit >= 5{
                percents["Flush"] = 100
            }
            else if totalMaxSuit == 4{
                percents["Flush"] = 35
            }
            else if totalMaxSuit == 3{
                percents["Flush"] = 4.2
            }
            //Pair
            if totalMaxValue >= 2{
                percents["Pair"] = 100
                if totalMaxValue >= 3{
                    percents["Set"] = 100
                    if totalMaxValue == 4 {
                        percents["Straight"] = 100
                    }
                }
                else{
                    percents["Set"] = 8.42
                }
                percents["TwoPair"] = 12.5
            }
            else{
                percents["Pair"] = 24.14
                percents["Set"] = 1.81
                percents["Straight"] = 0
            }
            if numPairs >= 2{
                percents["TwoPair"] = 100
            }
            else {
                percents["TwoPair"] = 2.36
            }

            if percents["Set"] == 100 && percents["Straight"] != 100{
                percents["Straight"] = 4.26
            }
            percents["StraightFlush"] = 100 * (0.01 * percents["Flush"]! * 0.01 * percents["Straight"]!)
        }
        else if board.count == 4{
            if totalMaxValue >= 2{
                percents["Pair"] = 100
                if totalMaxValue >= 3{
                    percents["Set"] = 100
                    if totalMaxValue == 4 {
                        percents["Straight"] = 100
                    }
                }
                else{
                    percents["Set"] = 4.3
                }
                percents["TwoPair"] = 6.5
            }
            if numPairs >= 2{
                percents["TwoPair"] = 100
            }
            if percents["Set"] == 100 && percents["Straight"] != 100{
                percents["Straight"] = 2.1
            }
            percents["StraightFlush"] = 100 * (0.01 * percents["Flush"]! * 0.01 * percents["Straight"]!)
        }
        else if board.count == 5{
            if totalMaxValue >= 2{
                percents["Pair"] = 100
                if totalMaxValue >= 3{
                    percents["Set"] = 100
                    if totalMaxValue == 4 {
                        percents["Straight"] = 100
                    }
                }
            }
            if totalMaxSuit >= 5{
                percents["FLush"] = 100
            }
            if numPairs >= 2 {
                percents["TwoPair"] = 100
            }
        }
        flushLabel.text = String(percents["Flush"]!) + "%"
        straightLabel.text = String(percents["Straight"]!) + "%"
        pairLabel.text = String(percents["Pair"]!) + "%"
        twopairLabel.text = String(percents["TwoPair"]!) + "%"
        setlabel.text = String(percents["Set"]!) + "%"
        straightflushLabel.text = String(percents["StraightFlush"]!) + "%"
        
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

}
