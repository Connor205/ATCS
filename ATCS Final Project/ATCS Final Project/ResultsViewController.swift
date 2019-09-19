//
//  ResultsViewController.swift
//  ATCS Final Project
//
//  Created by Connor Nelson on 3/19/19.
//  Copyright © 2019 Connor Nelson. All rights reserved.
//

import UIKit

class ResultsViewController: UIViewController {
    
    @IBOutlet weak var finalPercentageLabel: UILabel!
    var hand: [card] = []
    var board: [card] = []
    var attempting = ""
    var finalPercentage = 0.0
    override func viewDidLoad() {
        super.viewDidLoad()
        finalPercentage = calculatePercentage(attempting: attempting)
        print(finalPercentage)
        finalPercentageLabel.text = String(finalPercentage) + "%"

        // Do any additional setup after loading the view.
    }
    func calculatePercentage(attempting: String) -> Double{
        if attempting == "Flush"{
//            let hearts = 0
//            let spades = 0
//            let diamonds = 0
//            let clubs = 0
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
            if board.count == 0{
                if totalMaxSuit == 2{
                    return 23.59
                }
                else{
                    return 3.4
                }
            }
            if board.count == 3{
                if totalMaxSuit == 5{
                    return 100
                }
                else if totalMaxSuit == 4{
                    return 35
                }
                else if totalMaxSuit == 3{
                    return 4.2
                }
            }
        }
//        else if attempting == "Set"{
//            var valueCounts
//        }
        
        return 0.0
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
