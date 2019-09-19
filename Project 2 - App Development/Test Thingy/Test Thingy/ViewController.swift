//
//  ViewController.swift
//  Test Thingy
//
//  Created by Connor Nelson on 1/9/19.
//  Copyright © 2019 Connor Nelson. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    @IBAction func showAlert () {
        let alert = UIAlertController(title: "Hello World!", message: "This is cool", preferredStyle: .alert)
        let action = 
        alert.addAction(alert)
        present(alert, animated:true)
        
    }
}

