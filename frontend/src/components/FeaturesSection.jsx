import { ArrowPathIcon, WindowIcon, LockClosedIcon, BoltIcon } from '@heroicons/react/24/outline'

const features = [
  {
    name: 'Tezkor kirish',
    description:
      'Platformaga istalgan qurilmadan osongina kirib, darslaringizni davom ettiring.',
    icon: BoltIcon,
  },
  {
    name: 'Xavfsiz maʼlumotlar',
    description:
      'Maʼlumotlaringizni himoya qilish uchun zamonaviy xavfsizlik texnologiyalarini qo‘llaymiz.',
    icon: LockClosedIcon,
  },
  {
    name: 'Moslashtirilgan o‘quv rejasi',
    description:
      'O‘quv dasturlaringizni darajangiz va maqsadlaringizga moslashtiramiz.',
    icon: ArrowPathIcon,
  },
  {
    name: 'Interaktiv darslar',
    description:
      'Koreys tilini qiziqarli va samarali o‘rganish uchun interaktiv topshiriqlar va mashqlar.',
    icon: WindowIcon,
  },
]

export default function FeaturesSection() {
  return (
    <div className="bg-white py-16 sm:py-32">
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <div className="mx-auto max-w-2xl lg:text-center">
          <h2 className="text-base font-semibold text-indigo-600">Til o‘rganishni boshlang</h2>
          <p className="mt-2 text-4xl font-bold tracking-tight text-gray-900 sm:text-5xl">
            Koreys tilini o'rganish uchun barcha imkoniyatlar bir joyda
          </p>
          <p className="mt-6 text-lg text-gray-600">
            Bizning platformamiz yordamida koreys tilini tez va samarali o'rganing. Moslashtirilgan rejalar, 
            interaktiv mashg'ulotlar va xavfsiz xizmatlardan foydalaning.
          </p>
        </div>
        <div className="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-4xl">
          <dl className="grid max-w-xl grid-cols-1 gap-x-8 gap-y-10 lg:max-w-none lg:grid-cols-2 lg:gap-y-16">
            {features.map((feature) => (
              <div key={feature.name} className="relative pl-16">
                <dt className="text-lg font-semibold text-gray-900">
                  <div className="absolute left-0 top-0 flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-600">
                    <feature.icon aria-hidden="true" className="h-6 w-6 text-white" />
                  </div>
                  {feature.name}
                </dt>
                <dd className="mt-2 text-base text-gray-600">{feature.description}</dd>
              </div>
            ))}
          </dl>
        </div>
      </div>
    </div>
  )
}
