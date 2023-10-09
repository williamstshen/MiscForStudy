//
//  ViewController.swift
//  CatchTheAnimal
//
//  Created by William on 2023/10/9.
//
//  2023.10.09 : to try add function :
//      (1) slider instead of tap
//      (2) add buttons for "start" and "clear highest score"
//      (3) change hand code vars to arrays 

import UIKit

class ViewController: UIViewController {
    
    var score = 0
    var timer = Timer()
    var hideTimer = Timer()
    var counter = 0
    var highScore = 0
    
    var gsLadyArray = [UIImageView]()
    
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
        let storedHighestScore = UserDefaults.standard.object(forKey: "highest_score")
        if storedHighestScore == nil {
            highScore = 0
            highScoreLabel.text = "Highest Score: \(highScore)"
        }
        if let newScore = storedHighestScore as? Int {
            highScore = newScore
            highScoreLabel.text = "Highest Score: \(highScore)"
        }
        
        
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
        
        gsLadyArray = [gsLady1, gsLady2, gsLady3, gsLady4,
                       gsLady5, gsLady6, gsLady7, gsLady8,
                       gsLady9, gsLady10, gsLady11, gsLady12,
                       gsLady13, gsLady14, gsLady15, gsLady16,
        ]
        
        counter = 15
        timeLabel.text = "Time: \(counter)s"
        timer = Timer.scheduledTimer(timeInterval: 1, target: self, selector: #selector(countDown), userInfo: nil, repeats: true)
        hideTimer = Timer.scheduledTimer(timeInterval: 0.8, target: self, selector: #selector(gsLadyHidden), userInfo: nil, repeats: true)
        
        
    }
    
    @objc func gsLadyHidden() {
        for gslady in gsLadyArray {
            // hidden also means cannot catch tap gestures
            gslady.isHidden = true
        }
        
        let random_n = Int(arc4random_uniform(UInt32(gsLadyArray.count - 1)))
        gsLadyArray[random_n].isHidden = false
    }
    
    @objc func increaseScore() {
        score += 1
        scoreLabel.text = "Score: \(score)"
    }
    
    @objc func countDown() {
        counter -= 1
        timeLabel.text = "Time: \(counter)s"
        
        if counter == 0 {
            timer.invalidate()
            hideTimer.invalidate()
            
            if self.score > self.highScore {
                self.highScore = self.score
                self.highScoreLabel.text = "Highest Score: \(self.highScore)"
                UserDefaults.standard.set(self.highScore, forKey: "highest_score")
            }
            
            // send alert to player
            let alert = UIAlertController(title: "Time's Up", message: "Play Again?", preferredStyle: UIAlertController.Style.alert)
            let rpButton = UIAlertAction(title: "Replay", style: UIAlertAction.Style.default) { [self]
                (UIAlertAction) in
                // replay func
                // [WS] in closure func, need self to access correct global vars
                print("DBG : \(self.score)")
                self.score = 0
                self.scoreLabel.text = "Score: \(self.score)"
                self.counter = 15
                self.timeLabel.text = "Time: \(self.counter)s"
                self.timer = Timer.scheduledTimer(timeInterval: 1, target: self, selector: #selector(self.countDown), userInfo: nil, repeats: true)
                self.hideTimer = Timer.scheduledTimer(timeInterval: 0.8, target: self, selector: #selector(self.gsLadyHidden), userInfo: nil, repeats: true)
                
                
            }
            let noButton = UIAlertAction(title: "NO", style: UIAlertAction.Style.cancel, handler: nil)
            
            alert.addAction(rpButton)
            alert.addAction(noButton)
            
            self.present(alert, animated: true, completion: nil)
            
            
            
            
        }
    }


}

