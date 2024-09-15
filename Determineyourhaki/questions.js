const questions = [
    {
        question: "How do you approach a new challenge?",
        options: [
            { text: "Dive in with courage and determination.", value: "red" },
            { text: "Analyze the situation thoroughly before acting.", value: "blue" },
            { text: "Seek a balanced and thoughtful approach.", value: "green" },
            { text: "Use creativity and innovative ideas to solve it.", value: "yellow" }
        ]
    },
    {
        question: "What motivates you the most?",
        options: [
            { text: "Achieving significant goals and making an impact.", value: "red" },
            { text: "Gaining deeper understanding and insights.", value: "blue" },
            { text: "Personal development and achieving harmony.", value: "green" },
            { text: "Exploring new ideas and expressing joy.", value: "yellow" },
            { text: "Mastery and control over complex situations.", value: "black" },
            { text: "Discovering hidden truths and mysteries.", value: "purple" }
        ]
    },
    {
        question: "How do you handle criticism?",
        options: [
            { text: "Use it as a challenge to overcome with resilience.", value: "red" },
            { text: "Reflect deeply and use it for self-improvement.", value: "blue" },
            { text: "Seek to understand and adjust in a balanced way.", value: "green" },
            { text: "Approach it with an open mind and creativity.", value: "yellow" },
            { text: "Analyze its impact on your control and strategy.", value: "black" },
            { text: "Use intuition to gain insight from it.", value: "purple" },
            { text: "Maintain honesty and integrity while addressing it.", value: "white" }
        ]
    },
    {
        question: "What is your preferred method for solving problems?",
        options: [
            { text: "Act decisively and take bold actions.", value: "red" },
            { text: "Assess and reflect to understand all aspects.", value: "blue" },
            { text: "Apply practical solutions with empathy and balance.", value: "green" },
            { text: "Explore creative and enthusiastic solutions.", value: "yellow" },
            { text: "Use strategic control and analysis.", value: "black" },
            { text: "Rely on intuition and innovative thinking.", value: "purple" },
            { text: "Focus on clarity and straightforward solutions.", value: "white" }
        ]
    },
    {
        question: "How do you approach leadership?",
        options: [
            { text: "Lead with confidence and assertiveness.", value: "red" },
            { text: "Guide with insight and strategic thinking.", value: "blue" },
            { text: "Support and balance the team's needs.", value: "green" },
            { text: "Inspire and energize with creativity.", value: "yellow" },
            { text: "Maintain control and discipline to achieve goals.", value: "black" },
            { text: "Lead with vision and insight into deeper truths.", value: "purple" },
            { text: "Promote purity, fairness, and integrity.", value: "white" }
        ]
    },
    {
        question: "How do you handle stress?",
        options: [
            { text: "Confront it directly and manage it with determination.", value: "red" },
            { text: "Stay calm and analyze the situation rationally.", value: "blue" },
            { text: "Find a balanced approach to reduce stress.", value: "green" },
            { text: "Maintain optimism and look for creative solutions.", value: "yellow" },
            { text: "Use discipline and strategic control to manage it.", value: "black" },
            { text: "Trust your intuition to navigate through it.", value: "purple" },
            { text: "Seek peace and clarity to resolve it.", value: "white" }
        ]
    },
    {
        question: "What is your approach to personal growth?",
        options: [
            { text: "Pursue goals with ambition and determination.", value: "red" },
            { text: "Seek knowledge and reflect deeply.", value: "blue" },
            { text: "Focus on achieving harmony and balance.", value: "green" },
            { text: "Embrace creative exploration and joy.", value: "yellow" },
            { text: "Gain control and mastery over your abilities.", value: "black" },
            { text: "Discover deeper insights and spiritual growth.", value: "purple" },
            { text: "Uphold purity, honesty, and personal integrity.", value: "white" }
        ]
    },
    {
        question: "How do you express creativity?",
        options: [
            { text: "Through bold actions and daring ideas.", value: "red" },
            { text: "By reflecting deeply and finding profound solutions.", value: "blue" },
            { text: "By applying practical and balanced methods.", value: "green" },
            { text: "By exploring new and imaginative concepts.", value: "yellow" },
            { text: "By using control and precision in your work.", value: "black" },
            { text: "Through intuitive and visionary approaches.", value: "purple" },
            { text: "By seeking clarity and simplicity in your creations.", value: "white" }
        ]
    },
    {
        question: "How do you approach conflict resolution?",
        options: [
            { text: "Confront it with assertiveness and determination.", value: "red" },
            { text: "Understand all perspectives and mediate calmly.", value: "blue" },
            { text: "Seek a balanced and fair resolution.", value: "green" },
            { text: "Maintain a positive attitude and find creative solutions.", value: "yellow" },
            { text: "Exercise control and discipline to resolve it.", value: "black" },
            { text: "Use insight and intuition to guide the resolution.", value: "purple" },
            { text: "Adhere to your values and principles.", value: "white" }
        ]
    },
    {
        question: "What drives your decisions?",
        options: [
            { text: "A desire for achievement and making a significant impact.", value: "red" },
            { text: "A quest for deeper understanding and clarity.", value: "blue" },
            { text: "The need for stability and balanced outcomes.", value: "green" },
            { text: "The pursuit of joy and innovative experiences.", value: "yellow" },
            { text: "The aim for control and effective management.", value: "black" },
            { text: "The drive to uncover mysteries and explore deeper insights.", value: "purple" },
            { text: "The pursuit of clarity, purity, and integrity.", value: "white" }
        ]
    },
    {
        question: "What is your approach to team collaboration?",
        options: [
            { text: "Take initiative and lead the team with clear direction.", value: "red" },
            { text: "Observe and support team members to enhance collaboration.", value: "blue" },
            { text: "Ensure everyone’s voice is heard and maintain balance.", value: "green" },
            { text: "Encourage creativity and foster a collaborative environment.", value: "yellow" },
            { text: "Implement structured processes to guide the team.", value: "black" },
            { text: "Utilize deep insights to harmonize team efforts.", value: "purple" },
            { text: "Promote transparency and ethical practices within the team.", value: "white" }
        ]
    },
    {
        question: "How do you prioritize tasks?",
        options: [
            { text: "Focus on high-priority tasks that have the most impact.", value: "red" },
            { text: "Analyze and prioritize based on urgency and importance.", value: "blue" },
            { text: "Balance tasks based on immediate needs and long-term goals.", value: "green" },
            { text: "Use creativity to find innovative solutions to task management.", value: "yellow" },
            { text: "Apply strategic planning to ensure efficient task execution.", value: "black" },
            { text: "Trust your intuition to prioritize effectively.", value: "purple" },
            { text: "Maintain simplicity and clarity in your task management.", value: "white" }
        ]
    },
    {
        question: "How do you deal with uncertainty?",
        options: [
            { text: "Embrace it as an opportunity for growth and challenge.", value: "red" },
            { text: "Analyze available data to make informed decisions.", value: "blue" },
            { text: "Seek a balanced approach to manage and reduce uncertainty.", value: "green" },
            { text: "Use creative thinking to navigate through uncertain situations.", value: "yellow" },
            { text: "Apply control and strategic planning to mitigate risks.", value: "black" },
            { text: "Rely on intuition and flexibility to adapt to changes.", value: "purple" },
            { text: "Focus on maintaining clarity and stability in your approach.", value: "white" }
        ]
    },
    {
        question: "What is your strategy for learning new skills?",
        options: [
            { text: "Dive into practical experience and learn through doing.", value: "red" },
            { text: "Study and reflect deeply to understand the concepts.", value: "blue" },
            { text: "Balance theoretical knowledge with hands-on practice.", value: "green" },
            { text: "Explore new methods and maintain enthusiasm for learning.", value: "yellow" },
            { text: "Use strategic planning to master complex skills.", value: "black" },
            { text: "Trust intuitive learning methods and adapt as needed.", value: "purple" },
            { text: "Uphold a clear and structured approach to skill acquisition.", value: "white" }
        ]
    },
    {
        question: "How do you approach decision-making under pressure?",
        options: [
            { text: "Take decisive action with confidence and determination.", value: "red" },
            { text: "Analyze the situation thoroughly before making a decision.", value: "blue" },
            { text: "Seek a balanced approach to manage pressure effectively.", value: "green" },
            { text: "Use creativity and flexibility to adapt and make decisions.", value: "yellow" },
            { text: "Apply control and strategic thinking to handle pressure.", value: "black" },
            { text: "Rely on intuition and insight to guide your decisions.", value: "purple" },
            { text: "Focus on maintaining clarity and a calm mindset.", value: "white" }
        ]
    }
];
