//
//  BoardVC.swift
//  ATCS Final Project
//
//  Created by Connor Nelson on 3/18/19.
//  Copyright © 2019 Connor Nelson. All rights reserved.
//

import UIKit

class BoardVC: UIViewController {

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "home"{
            print("The Thing")
        }
        else if segue.identifier == "board" || segue.identifier == "hand"{
            let CardSelectionViewController = segue.destination as! CardSelectionViewController
            if segue.identifier == "board"{
                CardSelectionViewController.location = "board"
            }
            else{
                CardSelectionViewController.location = "hand"
            }
        }
        else
        {
            let HandChoosingVC = segue.destination as! HandChoosingVC
            HandChoosingVC.hand = hand
            HandChoosingVC.board = board
        }
    }
    @IBOutlet weak var boardLabel: UILabel!
    @IBOutlet weak var handLabel: UILabel!
    var hand: [card] = []
    var board: [card] = []
    var handLabelString = ""
    var boardLabelString = ""
    override func viewDidLoad() {

        super.viewDidLoad()
        boardLabel.text = boardLabelString
        handLabel.text = handLabelString

        // Do any additional setup after loading the view.
    }
    @IBAction func myUnwindAction(unwindSegue: UIStoryboardSegue){
        
    }
    func updateLabels(type: String){
        print("TESTING")
        print(handLabelString)
        print(boardLabelString)
        if type == "hand"{
            handLabelString = ""
            for i in hand{

                handLabelString = handLabelString + " " + i.suit[i.suit.startIndex...i.suit.startIndex] + i.value[i.value.startIndex...i.value.startIndex]
            }
        }
        else{
            boardLabelString = ""
            for i in board{

                boardLabelString = boardLabelString + " " + i.suit[i.suit.startIndex...i.suit.startIndex] + i.value[i.value.startIndex...i.value.startIndex]
            }
        }
        boardLabel.text = boardLabelString
        handLabel.text = handLabelString
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
