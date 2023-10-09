//
//  ViewController.swift
//  CatchTheAnimal
//
//  Created by Elaina mayo on 2023/10/9.
//

import UIKit

class ViewController: UIViewController {
    
    var score = 0
    
    @IBOutlet weak var timeLabel: UILabel!
    @IBOutlet weak var scoreLabel: UILabel!
    @IBOutlet weak var highScoreLabel: UILabel!
    @IBOutlet weak var gsLady2: UIImageView!
    @IBOutlet weak var gsLady1: UIImageView!
    @IBOutlet weak var gsLady3: UIImageView!
    @IBOutlet weak var gsLady4: UIImageView!
    @IBOutlet weak var gsLady5: UIImageView!
    @IBOutlet weak var gsLady6: UIImageView!
    @IBOutlet weak var gsLady7: UIImageView!
    @IBOutlet weak var gsLady8: UIImageView!
    @IBOutlet weak var gsLady9: UIImageView!
    @IBOutlet weak var gsLady10: UIImageView!
    @IBOutlet weak var gsLady11: UIImageView!
    @IBOutlet weak var gsLady12: UIImageView!
    @IBOutlet weak var gsLady13: UIImageView!
    @IBOutlet weak var gsLady14: UIImageView!
    @IBOutlet weak var gsLady15: UIImageView!
    @IBOutlet weak var gsLady16: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        gsLady1.isUserInteractionEnabled = true
        gsLady2.isUserInteractionEnabled = true
        gsLady3.isUserInteractionEnabled = true
        gsLady4.isUserInteractionEnabled = true
        gsLady5.isUserInteractionEnabled = true
        gsLady6.isUserInteractionEnabled = true
        gsLady7.isUserInteractionEnabled = true
        gsLady8.isUserInteractionEnabled = true
        gsLady9.isUserInteractionEnabled = true
        gsLady10.isUserInteractionEnabled = true
        gsLady11.isUserInteractionEnabled = true
        gsLady12.isUserInteractionEnabled = true
        gsLady13.isUserInteractionEnabled = true
        gsLady14.isUserInteractionEnabled = true
        gsLady15.isUserInteractionEnabled = true
        gsLady16.isUserInteractionEnabled = true
        
        scoreLabel.text = "Score: \(score)"
        let recgr1 = UITapGestureRecognizer(target: self, action: #selector(increaseScore))
        let recgr2 = UITapGestureRecognizer(target: self, action: #selector(increaseScore))
        let recgr3 = UITapGestureRecognizer(target: self, action: #selector(increaseScore))
        let recgr4 = UITapGestureRecognizer(target: self, action: #selector(increaseScore))
        let recgr5 = UITapGestureRecognizer(target: self, action: #selector(increaseScore))
        let recgr6 = UITapGestureRecognizer(target: self, action: #selector(increaseScore))
        let recgr7 = UITapGestureRecognizer(target: self, action: #selector(increaseScore))
        let recgr8 = UITapGestureRecognizer(target: self, action: #selector(increaseScore))
        let recgr9 = UITapGestureRecognizer(target: self, action: #selector(increaseScore))
        let recgr10 = UITapGestureRecognizer(target: self, action: #selector(increaseScore))
        let recgr11 = UITapGestureRecognizer(target: self, action: #selector(increaseScore))
        let recgr12 = UITapGestureRecognizer(target: self, action: #selector(increaseScore))
        let recgr13 = UITapGestureRecognizer(target: self, action: #selector(increaseScore))
        let recgr14 = UITapGestureRecognizer(target: self, action: #selector(increaseScore))
        let recgr15 = UITapGestureRecognizer(target: self, action: #selector(increaseScore))
        let recgr16 = UITapGestureRecognizer(target: self, action: #selector(increaseScore))
        
        gsLady1.addGestureRecognizer(recgr1)
        gsLady2.addGestureRecognizer(recgr2)
        gsLady3.addGestureRecognizer(recgr3)
        gsLady4.addGestureRecognizer(recgr4)
        gsLady5.addGestureRecognizer(recgr5)
        gsLady6.addGestureRecognizer(recgr6)
        gsLady7.addGestureRecognizer(recgr7)
        gsLady8.addGestureRecognizer(recgr8)
        gsLady9.addGestureRecognizer(recgr9)
        gsLady10.addGestureRecognizer(recgr10)
        gsLady11.addGestureRecognizer(recgr11)
        gsLady12.addGestureRecognizer(recgr12)
        gsLady13.addGestureRecognizer(recgr13)
        gsLady14.addGestureRecognizer(recgr14)
        gsLady15.addGestureRecognizer(recgr15)
        gsLady16.addGestureRecognizer(recgr16)
        
    }
    
    @objc func increaseScore() {
        score += 1
        scoreLabel.text = "Score: \(score)"
    }


}

