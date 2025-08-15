<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secondary Storage Devices</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.9.1/chart.min.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .presentation-container {
            max-width: 1200px;
            width: 90%;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }

        .slide {
            display: none;
            padding: 30px;
            min-height: 650px;
            animation: fadeIn 0.5s ease-in-out;
        }

        .slide.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        h1 {
            color: #333;
            font-size: 2.5em;
            margin-bottom: 20px;
            text-align: center;
            background: linear-gradient(45deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        h2 {
            color: #444;
            font-size: 2em;
            margin-bottom: 20px;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }

        h3 {
            color: #555;
            font-size: 1.5em;
            margin: 20px 0 10px 0;
            color: #667eea;
        }

        p, li {
            font-size: 1.1em;
            line-height: 1.6;
            color: #666;
            margin-bottom: 10px;
        }

        ul {
            padding-left: 20px;
        }

        /* Flow Diagram Styles */
        .flow-diagram {
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 30px 0;
            flex-wrap: wrap;
        }

        .flow-box {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 15px 25px;
            border-radius: 15px;
            margin: 10px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            min-width: 120px;
            text-align: center;
            font-weight: 600;
        }

        .flow-arrow {
            font-size: 2em;
            color: #667eea;
            margin: 0 10px;
        }

        /* Chart Container */
        .chart-container {
            background: white;
            border-radius: 15px;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }

        /* Comparison Table */
        .comparison-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        }

        .comparison-table th,
        .comparison-table td {
            padding: 15px 10px;
            text-align: center;
            border-bottom: 1px solid #ddd;
            font-size: 0.9em;
        }

        .comparison-table th {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            font-weight: 600;
        }

        .comparison-table tr:nth-child(even) {
            background-color: #f8f9fa;
        }

        /* Visual Icons for Storage Types */
        .storage-types {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }

        .storage-card {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
            text-align: center;
            transition: transform 0.3s ease;
        }

        .storage-card:hover {
            transform: translateY(-5px);
        }

        .storage-icon {
            font-size: 3em;
            margin-bottom: 15px;
        }

        /* HDD Diagram */
        .hdd-diagram {
            background: #f8f9fa;
            border-radius: 15px;
            padding: 30px;
            margin: 20px 0;
            text-align: center;
        }

        .hdd-parts {
            display: flex;
            justify-content: space-around;
            align-items: center;
            flex-wrap: wrap;
            margin: 20px 0;
        }

        .hdd-part {
            background: linear-gradient(135deg, #28a745, #20c997);
            color: white;
            padding: 15px;
            border-radius: 10px;
            margin: 10px;
            min-width: 120px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        /* SSD vs HDD Visual */
        .speed-comparison {
            display: flex;
            justify-content: space-around;
            margin: 30px 0;
        }

        .speed-bar {
            text-align: center;
        }

        .speed-visual {
            width: 60px;
            margin: 0 auto 10px;
            border-radius: 30px;
            position: relative;
            background: #e9ecef;
        }

        .speed-fill {
            border-radius: 30px;
            transition: height 2s ease;
        }

        .hdd-speed {
            height: 150px;
            background: #dc3545;
        }

        .ssd-speed {
            height: 150px;
            background: #28a745;
        }

        .ram-speed {
            height: 150px;
            background: #007bff;
        }

        /* Navigation */
        .navigation {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 40px;
            background: rgba(102, 126, 234, 0.1);
        }

        .nav-btn {
            padding: 12px 24px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-size: 1em;
            transition: all 0.3s ease;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        .nav-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        }

        .nav-btn:disabled {
            background: #ccc;
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        }

        .slide-counter {
            font-size: 1.1em;
            color: #667eea;
            font-weight: 600;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .slide {
                padding: 20px;
                min-height: 500px;
            }
            
            h1 {
                font-size: 2em;
            }
            
            h2 {
                font-size: 1.5em;
            }
            
            .flow-diagram {
                flex-direction: column;
            }
            
            .flow-arrow {
                transform: rotate(90deg);
            }
            
            .navigation {
                padding: 15px 20px;
            }
            
            .comparison-table th,
            .comparison-table td {
                padding: 10px 5px;
                font-size: 0.8em;
            }
        }
    </style>
</head>
<body>
    <div class="presentation-container">
        <!-- Slide 1: Title -->
        <div class="slide active">
            <div style="text-align: center; margin-top: 80px;">
                <h1>Secondary Storage Devices</h1>
                <p style="font-size: 1.3em; color: #667eea; margin: 30px 0;">"The Unsung Heroes of Our Digital Lives"</p>
                
                <div class="flow-diagram" style="margin-top: 50px;">
                    <div class="flow-box">💾 Storage Types</div>
                    <span class="flow-arrow">→</span>
                    <div class="flow-box">⚙️ How They Work</div>
                    <span class="flow-arrow">→</span>
                    <div class="flow-box">📊 Comparison</div>
                    <span class="flow-arrow">→</span>
                    <div class="flow-box">🚀 Applications</div>
                </div>
                
                <div style="margin-top: 60px; background: rgba(102, 126, 234, 0.1); padding: 20px; border-radius: 15px;">
                    <p style="font-size: 1.2em; color: #333;">
                        <strong>"Imagine if every time you turned off the lights, everything in your room disappeared forever..."</strong>
                    </p>
                </div>
            </div>
        </div>

        <!-- Slide 2: Introduction with Speed Chart -->
        <div class="slide">
            <h2>What are Secondary Storage Devices?</h2>
            <p style="font-size: 1.3em; color: #667eea; font-weight: bold;">
                "In 0.3 seconds (one blink), a modern SSD reads an entire book!"
            </p>
            
            <div class="speed-comparison">
                <div class="speed-bar">
                    <div class="speed-visual">
                        <div class="speed-fill hdd-speed" style="height: 30px;"></div>
                    </div>
                    <h4>HDD</h4>
                    <p>100 MB/s</p>
                </div>
                <div class="speed-bar">
                    <div class="speed-visual">
                        <div class="speed-fill ssd-speed" style="height: 100px;"></div>
                    </div>
                    <h4>SSD</h4>
                    <p>3,500 MB/s</p>
                </div>
                <div class="speed-bar">
                    <div class="speed-visual">
                        <div class="speed-fill ram-speed" style="height: 150px;"></div>
                    </div>
                    <h4>RAM</h4>
                    <p>25,000 MB/s</p>
                </div>
            </div>

            <h3>Five Key Characteristics:</h3>
            <ul>
                <li><strong>Non-volatile:</strong> Like digital tattoos - permanent until removed</li>
                <li><strong>Large capacity:</strong> Store 2 million books worth of data</li>
                <li><strong>Cost-effective:</strong> 1GB costs less than a candy bar</li>
                <li><strong>Slower access:</strong> Trade-off for permanence</li>
                <li><strong>Permanent storage:</strong> Survives power outages & coffee spills!</li>
            </ul>
        </div>

        <!-- Slide 3: Types with Visual Icons -->
        <div class="slide">
            <h2>Types of Secondary Storage</h2>
            
            <div class="storage-types">
                <div class="storage-card">
                    <div class="storage-icon">🧲</div>
                    <h3>Magnetic Storage</h3>
                    <p>Data stored as magnetic patterns</p>
                    <ul style="text-align: left;">
                        <li>Hard Disk Drives (HDD)</li>
                        <li>Magnetic Tape</li>
                        <li>Floppy Disks (obsolete)</li>
                    </ul>
                </div>
                
                <div class="storage-card">
                    <div class="storage-icon">💿</div>
                    <h3>Optical Storage</h3>
                    <p>Data as microscopic pits & bumps</p>
                    <ul style="text-align: left;">
                        <li>CD (Compact Disc)</li>
                        <li>DVD (Digital Video Disc)</li>
                        <li>Blu-ray Disc</li>
                    </ul>
                </div>
                
                <div class="storage-card">
                    <div class="storage-icon">⚡</div>
                    <h3>Solid State Storage</h3>
                    <p>Electronic switches, no moving parts</p>
                    <ul style="text-align: left;">
                        <li>SSD (Solid State Drive)</li>
                        <li>USB Flash Drives</li>
                        <li>Memory Cards</li>
                    </ul>
                </div>
                
                <div class="storage-card">
                    <div class="storage-icon">☁️</div>
                    <h3>Cloud Storage</h3>
                    <p>Remote servers, not actual clouds!</p>
                    <ul style="text-align: left;">
                        <li>Online storage services</li>
                        <li>Distributed storage</li>
                        <li>100,000+ drives working together</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- Slide 4: HDD Working with Diagram -->
        <div class="slide">
            <h2>How Hard Disk Drives Work</h2>
            <p style="color: #667eea; font-weight: bold;">
                "Heads fly 3 nanometers above spinning disks at 15,000 RPM - more precise than advanced aircraft!"
            </p>
            
            <div class="hdd-diagram">
                <h3>HDD Components & Process</h3>
                <div class="hdd-parts">
                    <div class="hdd-part">
                        <strong>Platters</strong><br>
                        Spinning disks<br>
                        15,000 RPM
                    </div>
                    <div class="hdd-part">
                        <strong>Read/Write Head</strong><br>
                        Flies 3nm above<br>
                        Reads magnetic patterns
                    </div>
                    <div class="hdd-part">
                        <strong>Actuator Arm</strong><br>
                        Positions head<br>
                        Ultra-precise movement
                    </div>
                    <div class="hdd-part">
                        <strong>Controller</strong><br>
                        Manages data flow<br>
                        Coordinates operations
                    </div>
                </div>
                
                <div class="flow-diagram">
                    <div class="flow-box">Data Request</div>
                    <span class="flow-arrow">→</span>
                    <div class="flow-box">Controller</div>
                    <span class="flow-arrow">→</span>
                    <div class="flow-box">Actuator Arm</div>
                    <span class="flow-arrow">→</span>
                    <div class="flow-box">Read/Write Head</div>
                    <span class="flow-arrow">→</span>
                    <div class="flow-box">Magnetic Pattern</div>
                </div>
            </div>
        </div>

        <!-- Slide 5: SSD Working -->
        <div class="slide">
            <h2>How Solid State Drives Work</h2>
            <p style="color: #667eea; font-weight: bold;">
                "Zero moving parts - pure electronic magic with billions of memory cells!"
            </p>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin: 30px 0;">
                <div style="background: #f8f9fa; padding: 20px; border-radius: 15px;">
                    <h3>SSD Components</h3>
                    <ul>
                        <li><strong>NAND Flash Memory:</strong> Billions of memory cells</li>
                        <li><strong>Controller:</strong> Traffic director for data</li>
                        <li><strong>Cache:</strong> Temporary high-speed storage</li>
                        <li><strong>Interface:</strong> SATA/NVMe connection</li>
                    </ul>
                </div>
                <div style="background: #f8f9fa; padding: 20px; border-radius: 15px;">
                    <h3>How It Works</h3>
                    <ul>
                        <li>Data stored as electrical charges</li>
                        <li>Memory cells = tiny batteries (charged/uncharged)</li>
                        <li>Controller manages wear leveling</li>
                        <li>No mechanical delays = instant access</li>
                    </ul>
                </div>
            </div>
            
            <div class="flow-diagram">
                <div class="flow-box">Data Request</div>
                <span class="flow-arrow">→</span>
                <div class="flow-box">SSD Controller</div>
                <span class="flow-arrow">→</span>
                <div class="flow-box">NAND Flash</div>
                <span class="flow-arrow">→</span>
                <div class="flow-box">Memory Cells</div>
                <span class="flow-arrow">→</span>
                <div class="flow-box">Instant Access!</div>
            </div>
        </div>

        <!-- Slide 6: Advantages with Cost Chart -->
        <div class="slide">
            <h2>Advantages of Secondary Storage</h2>
            <p style="color: #667eea; font-weight: bold;">
                "Your smartphone's storage would have cost $10 million in 1990!"
            </p>
            
            <div class="chart-container">
                <canvas id="costChart" width="400" height="200"></canvas>
            </div>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0;">
                <div style="background: #e8f5e8; padding: 20px; border-radius: 15px;">
                    <h3 style="color: #28a745;">✓ Key Benefits</h3>
                    <ul>
                        <li><strong>Non-volatile:</strong> Survives power loss</li>
                        <li><strong>Massive capacity:</strong> 4 million books per drive</li>
                        <li><strong>Ultra-reliable:</strong> 10+ years continuous operation</li>
                        <li><strong>Cost-effective:</strong> Million times cheaper than 1990</li>
                    </ul>
                </div>
                <div style="background: #f0f8ff; padding: 20px; border-radius: 15px;">
                    <h3 style="color: #007bff;">💡 Amazing Facts</h3>
                    <ul>
                        <li>SSDs survive freezing, heating, drops</li>
                        <li>Data centers: 100,000+ drives together</li>
                        <li>500,000 songs or 1,000 HD movies per drive</li>
                        <li>Some drives spin non-stop for decades</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- Slide 7: Disadvantages -->
        <div class="slide">
            <h2>Disadvantages of Secondary Storage</h2>
            <p style="color: #dc3545; font-weight: bold;">
                "Even superheroes have kryptonite!"
            </p>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 30px 0;">
                <div style="background: #ffe6e6; padding: 20px; border-radius: 15px;">
                    <h3 style="color: #dc3545;">⚠️ HDD Limitations</h3>
                    <ul>
                        <li><strong>Mechanical parts:</strong> Can break from drops</li>
                        <li><strong>Slow speed:</strong> 1000x slower than RAM</li>
                        <li><strong>Noise:</strong> Spinning disks make sound</li>
                        <li><strong>Power hungry:</strong> Motors need energy</li>
                        <li><strong>"Click of death":</strong> Mechanical failure</li>
                    </ul>
                </div>
                <div style="background: #fff0e6; padding: 20px; border-radius: 15px;">
                    <h3 style="color: #ff8c00;">⚠️ SSD Limitations</h3>
                    <ul>
                        <li><strong>Expensive:</strong> Higher cost per GB</li>
                        <li><strong>Write cycles:</strong> Limited lifetime writes</li>
                        <li><strong>Data recovery:</strong> Harder when failed</li>
                        <li><strong>Wear leveling:</strong> Complex management needed</li>
                    </ul>
                </div>
            </div>
            
            <div style="background: #f8f9fa; padding: 20px; border-radius: 15px; text-align: center;">
                <h3>Security Fact</h3>
                <p>"Deleted files often remain until overwritten - that's why high-security organizations physically shred drives into pieces smaller than 2mm!"</p>
            </div>
        </div>

        <!-- Slide 8: Comprehensive Comparison Table -->
        <div class="slide">
            <h2>Storage Device Comparison</h2>
            <p style="color: #667eea; font-weight: bold;">
                "From room-sized computers to pocket-sized powerhouses!"
            </p>
            
            <table class="comparison-table">
                <thead>
                    <tr>
                        <th>Device Type</th>
                        <th>Capacity Range</th>
                        <th>Speed (MB/s)</th>
                        <th>Cost/GB</th>
                        <th>Durability</th>
                        <th>Power Usage</th>
                        <th>Best Use Case</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>HDD</strong></td>
                        <td>500GB - 20TB</td>
                        <td>80-160</td>
                        <td>$0.02-0.05</td>
                        <td>Moderate</td>
                        <td>6-8W</td>
                        <td>Mass storage, backup</td>
                    </tr>
                    <tr>
                        <td><strong>SSD (SATA)</strong></td>
                        <td>128GB - 8TB</td>
                        <td>500-600</td>
                        <td>$0.08-0.15</td>
                        <td>High</td>
                        <td>2-3W</td>
                        <td>OS, applications</td>
                    </tr>
                    <tr>
                        <td><strong>SSD (NVMe)</strong></td>
                        <td>256GB - 8TB</td>
                        <td>2000-7000</td>
                        <td>$0.10-0.20</td>
                        <td>High</td>
                        <td>3-4W</td>
                        <td>Gaming, professional</td>
                    </tr>
                    <tr>
                        <td><strong>USB Flash</strong></td>
                        <td>4GB - 1TB</td>
                        <td>20-200</td>
                        <td>$0.15-0.50</td>
                        <td>Good</td>
                        <td>0.5W</td>
                        <td>Portable transfer</td>
                    </tr>
                    <tr>
                        <td><strong>Optical (DVD)</strong></td>
                        <td>4.7GB - 50GB</td>
                        <td>5-25</td>
                        <td>$0.01-0.02</td>
                        <td>Good</td>
                        <td>15-25W</td>
                        <td>Media, archival</td>
                    </tr>
                    <tr>
                        <td><strong>Cloud Storage</strong></td>
                        <td>Unlimited</td>
                        <td>Variable</td>
                        <td>$0.02-0.10/month</td>
                        <td>Very High</td>
                        <td>N/A</td>
                        <td>Backup, collaboration</td>
                    </tr>
                </tbody>
            </table>
            
            <div style="margin-top: 20px; text-align: center; background: #f0f8ff; padding: 15px; border-radius: 10px;">
                <p><strong>Mind-bending fact:</strong> All world data stacked as books would reach Earth to Moon 15 times!</p>
            </div>
        </div>

        <!-- Slide 9: Applications with Usage Chart -->
        <div class="slide">
            <h2>Applications & Use Cases</h2>
            <p style="color: #667eea; font-weight: bold;">
                "From Netflix streaming to Mars rovers - storage powers everything!"
            </p>
            
            <div class="chart-container">
                <canvas id="usageChart" width="400" height="200"></canvas>
            </div>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 20px 0;">
                <div style="background: #e8f5e8; padding: 20px; border-radius: 15px;">
                    <h3>🎮 Gaming Revolution</h3>
                    <ul>
                        <li><strong>Before:</strong> 30-60 sec loading times</li>
                        <li><strong>Now:</strong> 2-3 sec with SSD</li>
                        <li>PS5 custom SSD enables impossible experiences</li>
                        <li>No more loading screens needed!</li>
                    </ul>
                </div>
                
                <div style="background: #f0f8ff; padding: 20px; border-radius: 15px;">
                    <h3>🔬 Scientific Research</h3>
                    <ul>
                        <li><strong>Large Hadron Collider:</strong> 50 petabytes/year</li>
                        <li>Equivalent to 10 million HD movies annually</li>
                        <li>All from smashing particles together!</li>
                        <li>Enables incredible discoveries</li>
                    </ul>
                </div>
                
                <div style="background: #ffe6f0; padding: 20px; border-radius: 15px;">
                    <h3>🚀 Space Applications</h3>
                    <ul>
                        <li><strong>Mars rovers:</strong> Radiation-hardened storage</li>
                        <li>Slower than consumer devices</li>
                        <li>Survives cosmic radiation</li>
                        <li>Normal electronics would fry instantly!</li>
                    </ul>
                </div>
                
                <div style="background: #fff0e6; padding: 20px; border-radius: 15px;">
                    <h3>🌐 Everyday Impact</h3>
                    <ul>
                        <li><strong>Netflix:</strong> Specialized streaming drives</li>
                        <li><strong>Google:</strong> Global database queries</li>
                        <li>100,000+ drives working together</li>
                        <li>Powers our connected world</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- Slide 10: Conclusion with Evolution Timeline -->
        <div class="slide">
            <h2>Conclusion: The Digital Revolution</h2>
            <p style="color: #667eea; font-weight: bold; font-size: 1.3em;">
                "Your phone has more storage than the computers that sent humans to the moon!"
            </p>
            
            <div class="chart-container">
                <canvas id="evolutionChart" width="400" height="200"></canvas>
            </div>
            
            <div style="background: linear-gradient(135deg, #f8f9fa, #e9ecef); padding: 30px; border-radius: 20px; margin: 20px 0;">
                <h3 style="text-align: center; color: #667eea;">Key Takeaways</h3>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 20px;">
                    <div>
                        <h4>🔬 Scientific Marvel</h4>
                        <p>From room-sized machines to sugar-cube sized DNA storage</p>
                        
                        <h4>⚡ Speed Evolution</h4>
                        <p>From seconds to microseconds access times</p>
                    </div>
                    <div>
                        <h4>💰 Cost Revolution</h4>
                        <p>Million times cheaper than 30 years ago</p>
                        
                        <h4>🚀 Future Possibilities</h4>
                        <p>DNA molecules, individual atoms as storage</p>
                    </div>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 40px; padding: 30px; background: linear-gradient(135deg, #667eea, #764ba2); border-radius: 15px; color: white;">
                <h3>"Guardians of Our Digital Civilization"</h3>
                <p style="margin-top: 15px; color: #f8f9fa;">Every photo, document, and memory exists because these incredible devices never sleep, never forget, and keep getting better every year.</p>
            </div>
        </div>

        <div class="navigation">
            <button class="nav-btn" id="prevBtn" onclick="changeSlide(-1)">Previous</button>
            <span class="slide-counter">
                <span id="currentSlide">1</span> / <span id="totalSlides">10</span>
            </span>
            <button class="nav-btn" id="nextBtn" onclick="changeSlide(1)">Next</button>
        </div>
    </div>

    <script>
        let currentSlideIndex = 0;
        const slides = document.querySelectorAll('.slide');
        const totalSlides = slides.length;
        
        document.getElementById('totalSlides').textContent = totalSlides;

        function showSlide(n) {
            slides[currentSlideIndex].classList.remove('active');
            currentSlideIndex = n;
            
            if (currentSlideIndex >= totalSlides) {
                currentSlideIndex = totalSlides - 1;
            }
            if (currentSlideIndex < 0) {
                currentSlideIndex = 0;
            }
            
            slides[currentSlideIndex].classList.add('active');
            document.getElementById('currentSlide').textContent = currentSlideIndex + 1;
            
            // Update navigation buttons
            document.getElementById('prevBtn').disabled = currentSlideIndex === 0;
            document.getElementById('nextBtn').disabled = currentSlideIndex === totalSlides - 1;
            
            // Initialize charts when reaching specific slides
            if (currentSlideIndex === 5) {
                initCostChart();
            } else if (currentSlideIndex === 8) {
                initUsageChart();
            } else if (currentSlideIndex === 9) {
                initEvolutionChart();
            }
        }

        function changeSlide(direction) {
            showSlide(currentSlideIndex + direction);
        }

        // Cost Evolution Chart (Slide 6)
        function initCostChart() {
            const ctx = document.getElementById('costChart');
            if (ctx && !ctx.chart) {
                ctx.chart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: ['1990', '1995', '2000', '2005', '2010', '2015', '2020', '2025'],
                        datasets: [{
                            label: 'Cost per GB (USD)',
                            data: [10000, 1000, 100, 10, 1, 0.1, 0.05, 0.02],
                            borderColor: '#667eea',
                            backgroundColor: 'rgba(102, 126, 234, 0.1)',
                            tension: 0.4,
                            fill: true
                        }]
                    },
                    options: {
                        responsive: true,
                        plugins: {
                            title: {
                                display: true,
                                text: 'Storage Cost Evolution (Logarithmic Scale)',
                                font: { size: 16, weight: 'bold' }
                            },
                            legend: {
                                display: false
                            }
                        },
                        scales: {
                            y: {
                                type: 'logarithmic',
                                title: {
                                    display: true,
                                    text: 'Cost per GB (USD)'
                                }
                            },
                            x: {
                                title: {
                                    display: true,
                                    text: 'Year'
                                }
                            }
                        }
                    }
                });
            }
        }

        // Usage Applications Chart (Slide 9)
        function initUsageChart() {
            const ctx = document.getElementById('usageChart');
            if (ctx && !ctx.chart) {
                ctx.chart = new Chart(ctx, {
                    type: 'doughnut',
                    data: {
                        labels: ['Gaming', 'Cloud Services', 'Scientific Research', 'Enterprise', 'Personal Use', 'Media Streaming'],
                        datasets: [{
                            data: [20, 25, 15, 20, 15, 5],
                            backgroundColor: [
                                '#FF6384',
                                '#36A2EB',
                                '#FFCE56',
                                '#4BC0C0',
                                '#9966FF',
                                '#FF9F40'
                            ],
                            borderWidth: 2,
                            borderColor: '#fff'
                        }]
                    },
                    options: {
                        responsive: true,
                        plugins: {
                            title: {
                                display: true,
                                text: 'Storage Applications by Sector (%)',
                                font: { size: 16, weight: 'bold' }
                            },
                            legend: {
                                position: 'bottom'
                            }
                        }
                    }
                });
            }
        }

        // Storage Evolution Timeline Chart (Slide 10)
        function initEvolutionChart() {
            const ctx = document.getElementById('evolutionChart');
            if (ctx && !ctx.chart) {
                ctx.chart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: ['1956\nIBM 305', '1980\nSeagate ST-506', '1991\nFirst SSD', '2007\niPhone', '2020\nPS5 SSD', '2025\nModern NVMe'],
                        datasets: [{
                            label: 'Storage Capacity (GB)',
                            data: [0.005, 0.005, 0.02, 8, 825, 4000],
                            backgroundColor: [
                                'rgba(220, 53, 69, 0.8)',
                                'rgba(255, 193, 7, 0.8)',
                                'rgba(40, 167, 69, 0.8)',
                                'rgba(0, 123, 255, 0.8)',
                                'rgba(102, 126, 234, 0.8)',
                                'rgba(118, 75, 162, 0.8)'
                            ],
                            borderColor: [
                                '#dc3545',
                                '#ffc107',
                                '#28a745',
                                '#007bff',
                                '#667eea',
                                '#764ba2'
                            ],
                            borderWidth: 2
                        }]
                    },
                    options: {
                        responsive: true,
                        plugins: {
                            title: {
                                display: true,
                                text: 'Storage Evolution Timeline',
                                font: { size: 16, weight: 'bold' }
                            },
                            legend: {
                                display: false
                            }
                        },
                        scales: {
                            y: {
                                type: 'logarithmic',
                                title: {
                                    display: true,
                                    text: 'Capacity (GB)'
                                }
                            },
                            x: {
                                title: {
                                    display: true,
                                    text: 'Milestone Devices'
                                }
                            }
                        }
                    }
                });
            }
        }

        // Keyboard navigation
        document.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowRight' || e.key === ' ') {
                changeSlide(1);
            } else if (e.key === 'ArrowLeft') {
                changeSlide(-1);
            }
        });

        // Initialize
        showSlide(0);
    </script>
</body>
</html>
                
